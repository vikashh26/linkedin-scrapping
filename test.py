import requests
from bs4 import BeautifulSoup
import os

# # os.system("sudo service tor restart")


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


session = get_tor_session()
# # print(session.get("http://httpbin.org/ip").text)
# # # Above should print an IP different than your public IP

# # # Following prints your normal public IP
# # print(requests.get("http://httpbin.org/ip").text)

# # user_html = session.get("https://www.linkedin.com/in/kanikahanda2408?miniProfileUrn=urn:li:fs_miniProfile:ACoAAAQVlv0BwEe_2_6pDlh_Jy_RUd-EVrH9Qkc").text


# # html = open("testhml","w").write(user_html)




# # from main import WebDriver

# # driver= WebDriver()
# # driverinstance = driver.driver_instance

# # driverinstance.get("http://httpbin.org/ip")


# # ur = "https://www.linkedin.com/in/aashish-choudhary-97bb6a192?asdas"
# # print(ur.split("?")[0])


# import requests

# cookies = {
#     'bcookie': '"v=2&ba972245-cc38-48c1-8e2d-df8fffcbd4fe"',
#     'bscookie': '"v=1&20220325184911f7023e02-8653-4ae8-88fe-de772b4e4a2eAQGwKQ1H1zHYVBvLbpP3SbWugVevlgBa"',
#     'lidc': '"b=TGST05:s=T:r=T:a=T:p=T:g=2505:u=1:x=1:i=1648234151:t=1648320551:v=2:sig=AQGgC9Vt01rtoFKls5ckUIsJ_V3al3JB"',
#     'JSESSIONID': 'ajax:1100207725845381637',
#     'lang': 'v=2&lang=en-us',
#     'fid': 'AQH6E8DhfsY5qwAAAX_Ccc5XE-Dxqwl3n31RYxpODx3t_s85HWU6uwAmUZeoNxXHLiyoH7P2zc47Wg',
#     'G_ENABLED_IDPS': 'google',
#     'fcookie': 'AQHu9HX_UgU_5wAAAX_CcdnHoPdiFzhjMwE8kdpkXeSxHeoOtNyOz6dV22X7RiCr9WITr74ciN8sn8ZvVyJNzDmTQgpYfRVJu52ZxdnrPjjAhZIY4B-T52X-TwrtenU3x5VkPQUFylTxB6VzXVSr3kyvJIGUfaJQ1sAKqqBNL9Pp6Isl_QnH_VcDmG6tHJKjMOop4vov-xtLE48HGL5AtLEwhgxSTjZDqZb7FpCJ5-O1RARbF0nkbLzR0_E7hbRU0-u3-ujRY1iXRwZ7AeUq3MtT4-wUCBzKuenb12dNGJQpAPZafJbtVpJQdMoGVMJFOUZZ7Ah/YLWL3DD7oe4CB6/uW66azlZG4do4Jn1+P7ywI9YqQ==',
#     'ccookie': '0001AQH3A61IIGWM4wAAAX/CdkgwdCMT5g6d3qlEQWJBsuab4OqHTq25EIy3rsJRBzPPvLC13B2ydzHX/vuRWQuPYHMXdJqnY/3OIW6qErnwjiqXnyjEABCeP4w7WmWfHOJ+XkXWX31G8WZZ99nmwWHnQwtZZG+YRF30Q3Zh+xsn|50rGeV3+oi3pHrhgWKnVD+3RmHDIEXen9RN943byoFE=',
# }

# headers = {
#     'authority': 'in.linkedin.com',
#     'cache-control': 'max-age=0',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-dest': 'document',
#     'referer': 'https://in.linkedin.com/in/pranavkachhawa',
#     'accept-language': 'en-IN,en;q=0.9',
#     # Requests sorts cookies= alphabetically
#     # 'cookie': 'bcookie="v=2&ba972245-cc38-48c1-8e2d-df8fffcbd4fe"; bscookie="v=1&20220325184911f7023e02-8653-4ae8-88fe-de772b4e4a2eAQGwKQ1H1zHYVBvLbpP3SbWugVevlgBa"; lidc="b=TGST05:s=T:r=T:a=T:p=T:g=2505:u=1:x=1:i=1648234151:t=1648320551:v=2:sig=AQGgC9Vt01rtoFKls5ckUIsJ_V3al3JB"; JSESSIONID=ajax:1100207725845381637; lang=v=2&lang=en-us; fid=AQH6E8DhfsY5qwAAAX_Ccc5XE-Dxqwl3n31RYxpODx3t_s85HWU6uwAmUZeoNxXHLiyoH7P2zc47Wg; G_ENABLED_IDPS=google; fcookie=AQHu9HX_UgU_5wAAAX_CcdnHoPdiFzhjMwE8kdpkXeSxHeoOtNyOz6dV22X7RiCr9WITr74ciN8sn8ZvVyJNzDmTQgpYfRVJu52ZxdnrPjjAhZIY4B-T52X-TwrtenU3x5VkPQUFylTxB6VzXVSr3kyvJIGUfaJQ1sAKqqBNL9Pp6Isl_QnH_VcDmG6tHJKjMOop4vov-xtLE48HGL5AtLEwhgxSTjZDqZb7FpCJ5-O1RARbF0nkbLzR0_E7hbRU0-u3-ujRY1iXRwZ7AeUq3MtT4-wUCBzKuenb12dNGJQpAPZafJbtVpJQdMoGVMJFOUZZ7Ah/YLWL3DD7oe4CB6/uW66azlZG4do4Jn1+P7ywI9YqQ==; ccookie=0001AQH3A61IIGWM4wAAAX/CdkgwdCMT5g6d3qlEQWJBsuab4OqHTq25EIy3rsJRBzPPvLC13B2ydzHX/vuRWQuPYHMXdJqnY/3OIW6qErnwjiqXnyjEABCeP4w7WmWfHOJ+XkXWX31G8WZZ99nmwWHnQwtZZG+YRF30Q3Zh+xsn|50rGeV3+oi3pHrhgWKnVD+3RmHDIEXen9RN943byoFE=',
# }
# response = session.get('https://in.linkedin.com/in/pranavkachhawa', headers=headers, cookies=cookies)

# print(response.status_code)

