#!/bin/sh

curl -I --silent $1 | grep 'Location' | cut -d ' ' -f 2

