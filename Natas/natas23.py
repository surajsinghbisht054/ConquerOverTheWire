#!/usr/bin/python
import urllib
import urllib2
import cookielib
import httplib


# 
def request_generate(URL, cookie='', data={}):
    conn = httplib.HTTPConnection(URL)
    data=urllib.urlencode(data)
    req = {}
    req['User-Agent']    = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
    req['Authorization'] = 'Basic bmF0YXMyMjpjaEc5ZmJlMVRxMmVXVk1nallZRDFNc2ZJdk40NjFrSg=='
    req['Cookie']        = '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174;'+cookie
    req['Host']          = 'natas22.natas.labs.overthewire.org'
    req['Accept']        = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    req['Accept-Language'] ='en-US,en;q=0.5'
    req['Accept-Encoding']= 'gzip, deflate'
    req['Connection']     = 'keep-alive'
    conn.request("GET", "/index.php?revelio=true", headers=req)
    #help(conn.request)
    req = conn.getresponse()
    print req.read()
    conn.close()
    return req 


URL = 'natas22.natas.labs.overthewire.org'
s = request_generate(URL)
#print s.headers
#print s.info()
#print s.url
#print s.read()

