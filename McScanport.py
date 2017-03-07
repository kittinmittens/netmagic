#!/usr/bin/python3
#me@danielpeluso.com
##
import socket
import sys

dm = input("What domain would you like to scan??:")
stpt = int(input("Please enter a start port :"))
enpt = int(input("Please enter an end port :"))

def sc():
   for p in range(stpt, enpt):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.1)
      code = s.connect_ex( (dm, p) )
      if code == 0: 
         print(p, 'is open')

def main():
   sc()
#
##
if __name__ == '__main__':
    main()
      
