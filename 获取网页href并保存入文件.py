import requests
import re
import codecs

def gethtml():
    html = requests.get('http://sc.chinaz.com/tupian/beijingtupian.html').content
    html = html.decode('UTF-8')
    print(html)
    return html

def getimg(html):
    image = re.compile(r'[a-zA-z]+://[^\s\>\"\']*')
    imglist = re.findall(image, html)
    f = codecs.open("D:\highpython\Python-master\learn\9.txt", "w", "utf8")
    for imgurl in imglist:
        print(imgurl)
        f.write(imgurl + "\n")
    f.close()      
html = gethtml()
print(getimg(html))