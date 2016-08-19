import urllib, urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/5.0i (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
values = {'username': 'xxx', 'password': 'xxx'}
headers = {'User-Agent': user_agent, 'Referer':'http://www.zhihu.com/article'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
