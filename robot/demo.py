import urllib, urllib2

url = 'https://www.zhihu.com'
user_agent = 'Mozilla/5.0i (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
values = {'username': 'xxx', 'password': 'xxx'}
headers = {'User-Agent': user_agent, 'Referer': 'http://www.zhihu.com/article'}
data = urllib.urlencode(values)


# proxy
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


request = urllib2.Request(url, data, headers)
# timeout
# response = urllib2.urlopen('https://www.zhihu.com',timeout=10)
response = urllib2.urlopen(request)
print response.read()
