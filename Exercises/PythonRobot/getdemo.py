import urllib, urllib2

values = {}
values['username'] = 'xxx@xxx.com'
values['password'] = 'xxx'
data = urllib.urlencode(values)
url = 'http://xxx.xxx.com'
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
