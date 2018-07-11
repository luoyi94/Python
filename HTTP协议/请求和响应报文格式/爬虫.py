import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

html = response.read()

with open("1.tx","wb") as f:
    f.write(html)





