import urllib,urllib2

values = {"username":"xxx@xxx.com", "password":"xxx"}
data = urllib.urlencode(values)
url = "http://xxx.xxx.com"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
