import requests



def request(url,params=  None):
    cookies = {
        'fre': '0',
        'rd': '1380000',
        'zl': 'en',
        'fbtrack': 'bc78cb79705a8b8bdad492f0c6fae7fc',
        '_gid': 'GA1.2.2009349444.1779773701',
        '_gcl_au': '1.1.2107091175.1779773702',
        '_fbp': 'fb.1.1779773703040.687615060605590915',
        'expab': '1',
        'dpr': '2',
        'fbcity': '38',
        'ltv': '154469',
        'lty': '154469',
        'locus': '%7B%22addressId%22%3A0%2C%22lat%22%3A21.205806016854%2C%22lng%22%3A72.84030177766%2C%22cityId%22%3A38%2C%22ltv%22%3A154469%2C%22lty%22%3A%22point_of_interest%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A12305%2C%22fen%22%3A%22Surat+Junction%2C+Railway+Walking+Bridge%2C+Lambe+Hanuman+Rd%2C+Railway+Colony%2C+Varachha%2C+Surat%2C+Gujarat%22%7D',
        'uspl': 'true',
        '_ga_2NKE6R5GNY': 'GS2.2.s1779777700$o2$g1$t1779780041$j60$l0$h0',
        'ak_bmsc': '4796746A523C87C3668F63E25A4ADF75~000000000000000000000000000000~YAAQJRzFF/roWk6eAQAAhIfPYx9YpfmlvB9nSvvHCKu3q3xK0K7I5F3ugzE7mH8IC9l6JHq3RGTUpQMn9PGW9Cp1M5wjx3xHFOFqmlf9FA+j3esdriJF+eFLRlvuyd9mYt2D1uuiNKPUmmmzSR5+5wJsFxT4nzoYxCeuuyhqdhZZZqxbITNFDRz6f4pNPKnuOfdW3a86qUkWoWUT5rGFWb+n1/okvkvgfLane2uDi/eEt5LoG4UC3FaoTFhzl4j1VtjvN/mDPOg2YKG6rww3SGIx2R5MU41BWINKVZCDjzgs8bmwsp6HSdeb4DRJT3q/p7vJZ1DZB2oEY20IEmCX6WRUlqcLrB3GXtza1vQQDUwhJ0I5XKNSVLiAsm/YVk1nvSA=',
        'PHPSESSID': '14e64c71d140de6db4da7867cb0d9ed2',
        'csrf': 'a98ebd5316425fe0f33f0511ad7d0409',
        '_gat_global': '1',
        '_gat_country': '1',
        'AWSALBTG': 'suWjAhokM71MPnZ5f+hJ5uBk/ZO51ke9mKZJD2Tc7AiKG8jTlDgAytjxihQE6QzE4s+hZo2U9nwjmmlhPmzZpabr/k6/uk62UuELm3XDYulh67zMmepvAbYn8o38uV0bi7G0obS4slBjc9pfgm2ci7Q0mFb8QRHxnqWRWqHSYJer',
        'AWSALBTGCORS': 'suWjAhokM71MPnZ5f+hJ5uBk/ZO51ke9mKZJD2Tc7AiKG8jTlDgAytjxihQE6QzE4s+hZo2U9nwjmmlhPmzZpabr/k6/uk62UuELm3XDYulh67zMmepvAbYn8o38uV0bi7G0obS4slBjc9pfgm2ci7Q0mFb8QRHxnqWRWqHSYJer',
        '_ga_2XVFHLPTVP': 'GS2.1.s1779791012$o4$g1$t1779791072$j60$l0$h0',
        '_ga': 'GA1.1.980639559.1779773701',
        '_ga_X6B66E85ZJ': 'GS2.2.s1779791012$o3$g1$t1779791074$j60$l0$h0',
        'g_state': '{"i_l":0,"i_ll":1779791074526,"i_b":"VDkMi2hThUSNxZb2K9Aobe0lj5DQ2sNGPAfrXpS9hcY","i_e":{"enable_itp_optimization":0},"i_et":1779773702961}',
        '_dd_s': 'rum=0&expire=1779791971869',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        # 'cookie': 'fre=0; rd=1380000; zl=en; fbtrack=bc78cb79705a8b8bdad492f0c6fae7fc; _gid=GA1.2.2009349444.1779773701; _gcl_au=1.1.2107091175.1779773702; _fbp=fb.1.1779773703040.687615060605590915; expab=1; dpr=2; fbcity=38; ltv=154469; lty=154469; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A21.205806016854%2C%22lng%22%3A72.84030177766%2C%22cityId%22%3A38%2C%22ltv%22%3A154469%2C%22lty%22%3A%22point_of_interest%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A12305%2C%22fen%22%3A%22Surat+Junction%2C+Railway+Walking+Bridge%2C+Lambe+Hanuman+Rd%2C+Railway+Colony%2C+Varachha%2C+Surat%2C+Gujarat%22%7D; uspl=true; _ga_2NKE6R5GNY=GS2.2.s1779777700$o2$g1$t1779780041$j60$l0$h0; ak_bmsc=4796746A523C87C3668F63E25A4ADF75~000000000000000000000000000000~YAAQJRzFF/roWk6eAQAAhIfPYx9YpfmlvB9nSvvHCKu3q3xK0K7I5F3ugzE7mH8IC9l6JHq3RGTUpQMn9PGW9Cp1M5wjx3xHFOFqmlf9FA+j3esdriJF+eFLRlvuyd9mYt2D1uuiNKPUmmmzSR5+5wJsFxT4nzoYxCeuuyhqdhZZZqxbITNFDRz6f4pNPKnuOfdW3a86qUkWoWUT5rGFWb+n1/okvkvgfLane2uDi/eEt5LoG4UC3FaoTFhzl4j1VtjvN/mDPOg2YKG6rww3SGIx2R5MU41BWINKVZCDjzgs8bmwsp6HSdeb4DRJT3q/p7vJZ1DZB2oEY20IEmCX6WRUlqcLrB3GXtza1vQQDUwhJ0I5XKNSVLiAsm/YVk1nvSA=; PHPSESSID=14e64c71d140de6db4da7867cb0d9ed2; csrf=a98ebd5316425fe0f33f0511ad7d0409; _gat_global=1; _gat_country=1; AWSALBTG=suWjAhokM71MPnZ5f+hJ5uBk/ZO51ke9mKZJD2Tc7AiKG8jTlDgAytjxihQE6QzE4s+hZo2U9nwjmmlhPmzZpabr/k6/uk62UuELm3XDYulh67zMmepvAbYn8o38uV0bi7G0obS4slBjc9pfgm2ci7Q0mFb8QRHxnqWRWqHSYJer; AWSALBTGCORS=suWjAhokM71MPnZ5f+hJ5uBk/ZO51ke9mKZJD2Tc7AiKG8jTlDgAytjxihQE6QzE4s+hZo2U9nwjmmlhPmzZpabr/k6/uk62UuELm3XDYulh67zMmepvAbYn8o38uV0bi7G0obS4slBjc9pfgm2ci7Q0mFb8QRHxnqWRWqHSYJer; _ga_2XVFHLPTVP=GS2.1.s1779791012$o4$g1$t1779791072$j60$l0$h0; _ga=GA1.1.980639559.1779773701; _ga_X6B66E85ZJ=GS2.2.s1779791012$o3$g1$t1779791074$j60$l0$h0; g_state={"i_l":0,"i_ll":1779791074526,"i_b":"VDkMi2hThUSNxZb2K9Aobe0lj5DQ2sNGPAfrXpS9hcY","i_e":{"enable_itp_optimization":0},"i_et":1779773702961}; _dd_s=rum=0&expire=1779791971869',
    }

    response = requests.get(url, params=params,cookies=cookies, headers=headers)

    if response.status_code == 200:
        return response.text 

    else:
        print(response.status_code)
        print(response.text[:1000])
        return None 