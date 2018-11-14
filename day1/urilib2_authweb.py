# coding: utf-8


import urllib2

# urllib2urllib2.HTTPPasswordMgrWithDefaultRealm
# urllib2.ProxyBasicAuthHandler
# urllib2.ProxyBasicAuthHandler
# htpasswd -c /home/li/.htpasswd haha

test = 'test'
pawd = '123456'
# webserver = '123.57.245.206/polls/'
webserver = '192.168.21.52'

# 创建管理器
password_manger = urllib2.HTTPPasswordMgrWithDefaultRealm()
# 添加密码
password_manger.add_password(None, webserver, test, pawd)

# http基础验证处理器
httpauth_handler = urllib2.HTTPBasicAuthHandler(password_manger)

# proxy基础验证处理器
proxyauth_handler = urllib2.ProxyBasicAuthHandler(password_manger)

# opener = urllib2.build_opener(httpauth_handler)
# 构建自定义opener，支持多个处理器
opener = urllib2.build_opener(httpauth_handler, proxyauth_handler)

# 全局定义处理器,可选
# urllib2.install_opener(opener)

request = urllib2.Request('http://' + webserver)

# 自定义opener带有验证处理器请求
response = opener.open(request)

# 默认的请求
# response = urllib2.urlopen(request)

print response.read()

