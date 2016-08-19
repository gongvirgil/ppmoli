#!/usr/bin/env python
# -* - coding: UTF-8 -* -

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'email': '945257964@qq.com',
    'password': 'gong1993'
})
loginUrl = 'https://www.zhihu.com/login/email'
result = opener.open(loginUrl, postdata)
print result.read()
cookie.save(ignore_discard=True, ignore_expires=True)
gradeUrl = 'https://www.zhihu.com/people/mo-li-19-93'
result = opener.open(gradeUrl)
# print result.read()
