#!/usr/bin/python3

in_f = 'check.txt'
out_f = 'out.txt'

f = open(in_f, 'r', encoding='utf8')
in_utf = f.read()
f.close()

f = open(out_f, 'r', encoding='utf8')
out_utf = f.read()
f.close()

print("Input length: " + str(len(in_utf)))
print("Output length: " + str(len(out_utf)))

print('Looking for key match...')

for i in range(0, len(in_utf)):
    print(chr((ord(out_utf[i]) - ord(in_utf[i])) % 255), end="")
