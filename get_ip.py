#source : http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/

#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import fcntl
import struct
import sl_metro
import time

def param(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except IOError:
        return False


def waiting(ifname):
  metro = sl_metro.Metro(0.5)
  is_waiting = True

  while is_waiting:
    if metro.update():
      if param(ifname) == False:
        print "waiting for IP"
      else:
        is_waiting = False
        print "Got ip is : " , param(ifname)
        time.sleep(3)



