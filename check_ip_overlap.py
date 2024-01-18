#!/usr/bin/env python3.9
import ipaddr
n1 = ipaddr.IPNetwork('172.30.0.0/16')
n2 = ipaddr.IPNetwork('172.18.0.0/32')
x= n1.overlaps(n2);
print(x);