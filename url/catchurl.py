#-*- coding: utf-8 -*-

import requests
from lxml import html

USERNAME = "admin"
PASSWORD = "dfklsdjk16"

LOGIN_URL = "http://124.16.75.45/login"
URL = "http://124.16.75.45/FindUser"
URL2 = "http://124.16.75.45/register"
URL3 = "http://124.16.75.45/mgmtchpasswd"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authen_token = list(set(set(tree.xpath("//input[@name='csrf_token']/@value "))))[0]     #csrf_token 每次刷新页面都会生成一个新的字符串

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "csrf_token": authen_token
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    result2 = session_requests.get(URL2,headers = dict(referer = URL2))
    result3 = session_requests.get(URL3,headers = dict(referer = URL3) )
    print result3.content


if __name__ == '__main__':
    main()
















