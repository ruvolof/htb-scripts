#!/usr/bin/python3

import requests

target = 'http://10.10.10.168:8080/'
wordlist = '/usr/share/dirb/wordlists/common.txt'
filename = '/SuperSecureServer.py'

f = open(wordlist, 'r')
found = False
s = f.readline().strip()
while not found:
    url = target + s + filename
    res = requests.get(url)
    if res.status_code == 200:
        print("200 - " + url)
        found = True
    else:
        print(str(res.status_code) + ' - ' + url)
        s = f.readline().strip()
