#-*- coding: utf-8 -*-

#link: http://python.jobbole.com/83588/#article-comment
#link: https://github.com/kazuar/login_scraper_example/blob/master/login_scraper_example.py

import requests
from lxml import html

USERNAME = "admin"
PASSWORD = "password"

LOGIN_URL = "http://192.168.30.100/login"
URL = "http://192.168.30.100/FindUser"
URL2 = "http://192.168.30.100/register"
URL3 = "http://192.168.30.100/mgmtchpasswd"

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
