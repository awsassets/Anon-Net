#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import sys
import pyfiglet 
import datetime
import re

#PATH
path = os.getcwd()
torrc = (path+'/conf/torrc')
config = (path+'/conf/config')


ascii_banner = pyfiglet.figlet_format("Anon-Net") 
print(ascii_banner) 


port = input("[+] Please enter your Socks5 proxy service port: ")
time = input("[+] Please enter the time  to reset the IP address (it is recommended to be greater than 30s, less than 180s): ")

#Specify Socks proxy port

seconds=int(time)
fopen=open(torrc,'r')
 
w_str=""
for line in fopen:
         if re.search('MaxCircuitDirtiness',line):
                 line=re.sub('^MaxCircuitDirtiness.*','MaxCircuitDirtiness '+str(seconds),line)
                 w_str+=line
         else:
                 w_str+=line
wopen=open(torrc,'w')
wopen.write(w_str)
fopen.close()
wopen.close()


#Specify torroc file to start


fopen=open(torrc,'r')
 
w_str=""
for line in fopen:
         if re.search('Socks5Proxy 127.0.0.1:',line):
                 line=re.sub('^Socks5Proxy 127.0.0.1:.*','Socks5Proxy 127.0.0.1:'+str(port),line)
                 w_str+=line
         else:
                 w_str+=line
wopen=open(torrc,'w')
wopen.write(w_str)
fopen.close()
wopen.close()




#Start Tor
os.system("sudo cp %s /etc/polipo/config" %(config))
os.system("polipo")
os.system('sudo pkill tor')
os.system('{ nohup tor -f %s & } &>/dev/null' %(torrc))


#INFO
os.system("mate-terminal -e 'bash -c \"bash ipinfo.sh; exec bash\"'")