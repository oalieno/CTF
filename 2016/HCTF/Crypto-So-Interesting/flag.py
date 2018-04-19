#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

def get_flag(token):
	with open('/home/RSA/flag') as f:
		flags = json.loads(f.read())
	return flags[token]
