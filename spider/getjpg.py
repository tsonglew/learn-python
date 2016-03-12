import urllib, re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for i in imglist:
        urllib.urlretrieve(i, 'picgot/%s.jpg' % x)
        x += 1
    return "All pictures have been got!"

html = getHtml("http://tieba.baidu.com/p/2460150866")

print getImg(html)
