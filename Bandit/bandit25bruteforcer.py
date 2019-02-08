#!/usr/bin/python
import socket

def connection(passcode):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 30002))

    print s.recv(len('I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.\n'))

    s.send("UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ {}\n".format(passcode))
    print s.recv(1024)
    s.close()
    return

# main function
def main():
    connection(1)
    
    return

if __name__=='__main__':
    main()
