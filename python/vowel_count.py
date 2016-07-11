#!/usr/bin/env python
# -* - coding: UTF-8 -* -
str = raw_input(u"请输入字符串:".encode("GBK"))
vowel = 'aeiou'
total = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for s in str:
    if s in vowel:
        total += 1
        if s == 'a':
            a += 1
        elif s == 'e':
            e += 1
        elif s == 'i':
            i += 1
        elif s == 'o':
            o += 1
        elif s == 'u':
            u += 1
print total
print a
print e
print i
print o
print u
