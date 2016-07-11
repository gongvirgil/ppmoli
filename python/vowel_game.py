#!/usr/bin/env python
# -* - coding: UTF-8 -* -
str = raw_input(u"请输入字符串:".encode("GBK"))
vowel = 'aeiou'
p = -1
for i in str:
    if i not in vowel:
        p = str.index(i)
        break
print str[0:p] + str[p + 1:] + '-' + str[p] + 'ay'
