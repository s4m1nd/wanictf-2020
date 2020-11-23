#!/usr/bin/env python3
# coding: utf-8

import string
import itertools

#debug
#KEY = "REDACTED"
#print(KEY[0:3] * 19)

#print(len("REDREDREDREDREDREDREDREDREDREDREDREDREDREDREDREDREDREDRED"))

#print(string.printable)

keywords = [''.join(i) for i in itertools.product(string.printable, repeat = 3)]

#debug

f = open("output.txt", "rb").read()

def decrypt(key, flag):
    #assert(len(key) == len(flag))
    return bytes([_a ^ _b for _a, _b in zip(key, flag)])

def encrypt(s1, s2):
    assert(len(s1) == len(s2))
    result = ""
    for c1, c2 in zip(s1, s2):
        result += chr(ord(c1) ^ ord(c2))
    return result

for key in keywords:
    bKEY = bytes(key*19, 'utf-8')
    bCIPHER = f
    d = decrypt(bKEY, bCIPHER)
    #print(d)
    if b"FLAG" in d:
        print(d)



