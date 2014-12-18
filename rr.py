#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reboot your netgear router
__author__ = 'Andrea Pozzato'

import getpass
import urllib2
import subprocess
from time import sleep

ip=raw_input("ip:")
user=raw_input("user:")
psw=getpass.getpass("password:")

def alive(ip):
   out=subprocess.call("ping -o -c 1 %s" % ip, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
   if out==0:
       print ip+": is alive"
       print "reboot..."
       return 0
   else:
       print ip+" did not respond"
       return 1

def rebirth(ip):
    out=1
    i=0
    limit=20
    while out==0 | i<=limit:
        out=subprocess.call("ping -o -c 1 %s" % ip, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        i += 1
        print i,
        sleep(1)
    if i>=limit | out!=0:
        print "Call the police "+ip+" wasn't back!"
    else:
        print "Now "+ip+" is back"

def router_reboot(ip,user,psw):
    url="http://"+ip+"/"
    passman=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None,url,user,psw)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
    command=url+"setup.cgi?todo=reboot"
    #print(command)
    req=urllib2.urlopen(command)
    sleep(50)

rebirth(ip)
if alive(ip)==0:
     router_reboot(ip,user,psw)
     rebirth(ip)
     print("Done!")
else:
   print("Exit!")
