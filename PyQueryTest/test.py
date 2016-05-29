#-*- coding: utf-8 -*-

# Four methods to initialize PyQuery

# 1. init with string
# from pyquery import PyQuery as pq
# doc = pq('<html></html>')

# 2. init with lxml.etree
# from lxml import etree
# doc = pq(etree.fromstring("<html></html>"))

# 3. init directly with URL
# from pyquery import PyQuery as pq
# doc = pq('http://www.baidu.com')

# 4. init with file
# from pyquery import PyQuery as pq
# doc = pq(filename='hello.html')

from pyquery import PyQuery as pq

doc = pq(filename='hello.html')
print doc.html()
print '-'*40
print type(doc)
print '-'*40
li = doc('li')
print '-'*40
print type(li)
print '-'*40
print li.text()

# url for the passage: http://python.jobbole.com/85222/
