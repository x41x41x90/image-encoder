#!/usr/bin/env python
import sys
from zlib import decompress as d, compress as c
from base64 import b64decode as b, b64encode as e

def encode(fn, fo, ms):
	a = open (fn, "rb").read()
	l = len(a)
	a += "\xd9\xff\x24\x42\x00\x00"
	msg = ms
	a +=c(e(msg))
	a += "\xff\xd9"
	open (fo, "wb").write(a)

def decode(fn):
	a = open (fn, "rb").read()
	if a.find("\xd9\xff\x24\x42\x00\x00") != -1:
		msg = b(d(a[a.find("\xd9\xff\x24\x42\x00\x00")+6:-2]))
		print"[+] " + msg
	else:
		print ":("

if sys.argv[1] == "e":
	encode(sys.argv[2], sys.argv[3], sys.argv[4])

if sys.argv[1] == "d":
	decode (sys.argv[2])