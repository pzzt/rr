#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reboot your netgear router
__author__ = 'Andrea Pozzato'

import getpass
import urllib2
# import subprocess

ip=raw_input("ip:")
user=raw_input("user:")
psw=getpass.getpass("password:")

# def lookup(ip):
#
#     # miserve una funzione che restituisca 1 o 0
#     # a seconda se l'host è online o meno possibilmente senza doverla svrivere a mano
#     # utilizzando le socket. subprocess sostituisce la lib os.
#
#     output = subprocess.Popen(["ping", "-o", "-c3", "-W3000", ip],stdout=subprocess.PIPE).communicate()[0]
#     print(output)
#     if ("" in output):
#         print(ip+"is offline!")

def router_reboot(ip,user,psw):
    url="http://"+ip+"/"
    passman=urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None,url,user,psw)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
    comando=url+"setup.cgi?todo=reboot"
    #print(comando)
    req=urllib2.urlopen(comando)

router_reboot(ip,user,psw)
