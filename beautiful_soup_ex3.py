import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType' : 'general',
    'id': 'asdfda',
    'password': 'asdfd'
}

headers = {
    "User-Agent" : UserAgent().chrome,
    "Referere" : "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danwa.com%2F"
}

with req.session() as s:
    res = s.post('https://auth.danawa.com/login', login_info, headers=headers)

    if res.status_code != 200 :
        raise Exception("Login Failed!")

    # print(res.content.decode('UTF-8'))

    res = s.get('https://buyer.danawa.com/order/Order/orderList',headers=headers)

    # res.encoding = 'euc-kr'

    # print(res.text)

    soup = BeautifulSoup(res.text,'html.parser')

    check_name = soup.fild('p', class_='user')
    print(check_name)

    if check_name is None:
        raise Exception("Login Failed. Wrong Password.")
    
    info_list = soup.select("div.my_info > div.sub_info > ul.info_list > li")

    print(info_list)

    print("***** My Info *****")

    for v in info_list:
        proc, val = v.find('span').string.strip(), v.find('strong').string.strip()
        print('{} : {}'.format(proc,val))

