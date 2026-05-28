from request_data import request 
from lxml import html 
import re 
import json 
from urllib.parse import urljoin



def get_page_json(url):
    data = request(url)
    tree = html.fromstring(data)
    script = tree.xpath("//script/text()")
    for s in script:
        if 'window.__PRELOADED_STATE__' in s[:1000]:
            match = re.search(r'JSON\.parse\("(.*)"\)', s)
            json_str = match.group(1)
            json_str = bytes(json_str, "utf-8").decode("unicode_escape")
            json_str = json_str.encode("latin1").decode("utf-8")
            break

    resturant_response = json.loads(json_str)

    return resturant_response     


def parser(url):
    #overview request

    page_json = get_page_json(url)

    images = []
    proper_time = []

    orders_result = None
    if page_json.get('pages'):
        outlet = page_json.get('pages').get('current').get('pageTitle')
        res_id = page_json.get('pages').get('current').get('resId')
        page_url = page_json.get('pages').get('current').get('canonicalUrl')

        res_data_path = page_json.get('pages').get('restaurant').get(str(res_id)).get('sections')

        basic_info_path = res_data_path.get('SECTION_BASIC_INFO')

        dinein_rating = float(basic_info_path.get('rating_new').get('ratings').get('DINING').get('rating',0)) or 0
        dinein_review = float(basic_info_path.get('rating_new').get('ratings').get('DINING').get('reviewCount',0).replace(',','')) or 0
        delivery_rating = float(basic_info_path.get('rating_new').get('ratings').get('DELIVERY').get('rating',"0")) or 0
        delivery_review = float(basic_info_path.get('rating_new').get('ratings').get('DELIVERY').get('reviewCount',0).replace(',','')) or 0
        open_status = basic_info_path.get('res_status_text') or None
        timing = basic_info_path.get('timing').get('customised_timings').get('opening_hours') or None
        day_map = {
            "mon": "Monday",
            "tue": "Tuesday",
            "wed": "Wednesday",
            "thu": "Thursday",
            "fri": "Friday",
            "sat": "Saturday",
            "sun": "Sunday"
        }

        keys = list(day_map)
        timing = basic_info_path.get('timing', {}).get('customised_timings', {}).get('opening_hours', [])
        for item in timing:
            d = item.get('days', '').lower().split('-')
            t = item.get('timing')

            start = keys.index(d[0])
            end = keys.index(d[-1])
            print(start,end)
            rng = keys[start:end+1] if start <= end else keys[start:] + keys[:end+1]
            print(rng)
            proper_time += [{'day': day_map[x], 'timing': t} for x in rng]
                    

        res_info = res_data_path.get('SECTION_RES_DETAILS')
        facility = [i.get('text') for i in res_info.get('HIGHLIGHTS').get('highlights')]
        cusine = [i.get('name') for i in res_info.get('CUISINES').get('cuisines')]
        two_persone_data = res_info.get('CFT_DETAILS').get('cost_text_min_info')

        contanct_details = res_data_path.get('SECTION_RES_CONTACT')
        pincode = int(contanct_details.get('zipcode')) or None
        lat = float(contanct_details.get('latitude')) or None
        lng = float(contanct_details.get('longitude')) or None
        map_url = contanct_details.get('static_map_url') or None
        address = contanct_details.get('address') or None
        phone_no =contanct_details.get('phoneDetails').get('phoneStr') or None

        offer_path = res_data_path.get('SECTION_DINING_OFFERS')
        offers = []

        if offer_path:
            for o in offer_path:
                if not isinstance(o, dict):
                    continue

                offer_details = o.get('offerDetails') or {}
                assets = offer_details.get('assets') or {}

                offers.append({
                    'header': o.get('title'),
                    'expiry_date': o.get('end_time'),
                    'cupone_code': assets.get('voucher_code'),
                    'offer_value':assets.get('offer_value') if assets.get('offer_value') else offer_details.get('offerVal'),
                    'terms': assets.get('terms')
                })

    # order api 

    order_url = f"https://www.zomato.com/webroutes/getPage?page_url={url.replace('info','').split('https://www.zomato.com/')[1]}/order&location=&isMobile=0"    
    order_api_response = request(order_url)
    order_api_response = json.loads(order_api_response)
    if order_api_response.get('page_data'):
        menu_main_path = (
            (order_api_response.get('page_data') or {})
            .get('order') or {}
        )

        menu_main_path = (menu_main_path.get('menuList') or {}).get('menus') or []
        menu_list = []

        for menu_data in menu_main_path:
            menu_name = menu_data["menu"]["name"]
            menu_dict = {
                "menu_name": menu_name,
                "items": []
            }
            categories = menu_data["menu"].get("categories", [])
            for category_data in categories:
                items = category_data["category"].get("items", [])
                for item_data in items:
                    item = item_data["item"]
                    menu_dict["items"].append({
                        "name": item.get("name"),
                        "description":item.get("desc") if item.get("desc") else None,
                        "imageurl": item.get("item_image_url") if item.get("item_image_url") else None
                    })
            menu_list.append(menu_dict)

            orders_result = {
                "menu_list":menu_list
            }

    #photo api

    params = {
        'category': 'all',
        'res_id': f'{str(res_id)}',
        'page': '1',
        'limit': '40',
    }
    photo_url = f"https://www.zomato.com/webroutes/photos/loadMore"   

    while True:
        photos_request = request(photo_url,params=params)
        photos_request = json.loads(photos_request)
        number_of_pages = photos_request.get('page_data').get('sections').get('SECTION_GALLERY_PHOTOS').get('numberOfPages')

        if int(params['page']) > number_of_pages:
            break

        if not photos_request:
            break

        if photos_request.get('page_data').get('sections'):
            photo_path =photos_request.get('page_data').get('sections')
            image_ids = photo_path.get('SECTION_GALLERY_PHOTOS').get('entities')
            if image_ids:
                main_img_path = photos_request.get('entities').get('IMAGES')
                for i in image_ids:
                    if i.get('entity_type') == 'IMAGES':
                        ids = i.get('entity_ids')
                        for id in ids:
                            images.append(main_img_path.get(id).get('url'))
                print(params['page'])
                params['page'] = str(int(params['page']) + 1)
            else:
                break
        else:
            break

    #menu api 
    menu_images = []
    menu_url = f"https://www.zomato.com/webroutes/getPage?page_url={url.replace('info','').split('https://www.zomato.com/')[1]}/menu&location=&isMobile=0"    
    menu_api_response = request(menu_url)
    menu_api_response = json.loads(menu_api_response)
    if menu_api_response.get('page_data').get('sections'):
        menu_path =menu_api_response.get('page_data').get('sections').get('SECTION_IMAGE_MENU').get('menuItems')
        for m in menu_path:
            menu_images.append({
                'lable':m.get('label'),
                'images':[i.get('url') for i in m.get('pages')]
            })

    return {
        'res_id':res_id,
        'resturant_name':outlet,
        'page_url':page_url,
        'dining_rating':dinein_rating,
        'dinein_rating_count':dinein_review,
        'delivery_rating':delivery_rating,
        'delivery_rating_count':delivery_review,
        'status':open_status,
        'store_timing':proper_time,
        'map_url':map_url,
        'images':images,
        'address':address,
        'lng':lng,
        'lat':lat,
        'phone_no':phone_no,
        'pincode':pincode,
        'cusine':cusine,
        'facility':facility,
        'menu_images':menu_images[0].get('images'),
        'cost_for_two':two_persone_data or None,
        'menu_list':orders_result.get('menu_list') if orders_result else None,
        'offers':offers or None,
    }
