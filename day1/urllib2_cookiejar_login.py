# coding: utf-8

import urllib
import urllib2
import cookielib

# 构建一个cookiejar()对象，用来保存cookie
cookie = cookielib.CookieJar()

# 构建处理器对象，用来处理cookie
# 参数就是构建的cookiejar对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)


opener.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")]

url = "http://www.renren.com/PLogin.do"

data = {"email": '', "password": ""}

# 编码请求数据
data = urllib.urlencode(data)

request = urllib2.Request(url=url, data=data)

response = opener.open(request)

print response.read()

