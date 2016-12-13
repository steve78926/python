#-*- coding: utf8 -*-
# envir: win10

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print ('Get: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print ('%d bytes recived from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f,'http://www.python.org'),
        gevent.spawn(f,'https://www.yahoo.com'),
        gevent.spawn(f, 'https://github.com'),
])