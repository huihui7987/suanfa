import urllib

req = urllib.Request('http://www.baidu.com')
res = urllib.urlopen(req)
print (res.read())

import cookielib