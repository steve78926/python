#!/usr/bin/python
#coding=utf-8

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import re

hosturl = 'http://124.16.75.45/login'
posturl = 'http://124.16.75.45/login'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
           'Referer': "http://124.16.75.45/register"
            }
postData = {'csrf_token':"1488074911.19##3afab9b259d797d928cb7d81798abb75dae633d2",
            'username':"admin",
            'password':"dfklsdjk16",
            'submit':"登录"
            }

postData = urllib.urlencode(postData)
request = urllib2.Request(posturl, postData, headers)
#print request
response = urllib2.urlopen(request)
text = response.read()
print response
response2 = urllib2.urlopen('http://124.16.75.45/mgmtchpasswd')
print response2
text2 = response2.read()
print text2
