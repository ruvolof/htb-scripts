#!/usr/bin/env bash

DIR=/root/zettasync

rm -rv $DIR
mkdir $DIR

IP="[dead:beef::250:56ff:feb9:235f]"
PORT=8730

dirs='directories.txt'

while IFS= read -r D
do
  echo "Trying $D"
  rsync -av rsync://$IP:$PORT/$D $DIR/$D
done < "$dirs"
