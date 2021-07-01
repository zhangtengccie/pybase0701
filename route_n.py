#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng


import os
import re

str = '''
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.13.254  0.0.0.0         UG    100    0        0 eth0
192.168.13.0    0.0.0.0         255.255.255.0   U     100    0        0 eth0'''


re1 = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str)
print('网关为：'+re1[1])



