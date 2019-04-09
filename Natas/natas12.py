#!/usr/bin/python
import sys
import base64
import urllib



default_data = '{"showpassword":"no","bgcolor":"#ffffff"}'
required_data = '{"showpassword":"yes","bgcolor":"#ffffff"}'
def xor(data, key):
    out = ''
    for n, i in enumerate(data):
        out += chr(ord(i) ^ ord(key[n % len(key)]))
    return out

def decode(cookie):
    cookie  = base64.b64decode(cookie)
    print "[*] Base64 Cookie Reverse : ", cookie
    key = xorencryption(cookie)
    print "[*] Key Successfully Extracted : ", key
    print "[*] Exact Key ", key[:4]
    now = xor(required_data, key[:4])
    print "[*] Set Your Cookie Value : ", base64.b64encode(now)
    return


def xorencryption(cipher):
    key = ''
    for c,o in zip(cipher, default_data):
        print " %10d %10d" % (ord(c), ord(o))
        key+= chr(ord(c) ^ ord(o))

    print [key]
    return key

def main():
    if len(sys.argv)!=2:
        print "[*] Usages : "
        print "             {} DATA_COOKIE_VALUE".format(sys.argv[0])
        exit(0)

    cookie = urllib.unquote(sys.argv[1])
    print "[*] Cookie Value : ", cookie
    decode(cookie)
    return

if __name__=='__main__':
    main()
