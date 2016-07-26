#!/usr/bin/env python
# -* - coding: UTF-8 -* -
print u"------拉丁猪文字游戏------".encode("GBK")
str = raw_input(u"请输入一个单词:".encode("GBK"))
vowel = 'aeiou'
p = -1
for i in str:
    if i not in vowel:
        p = str.index(i)
        break
print u"结果为:".encode("GBK"), str[0:p] + str[p + 1:] + '-' + str[p] + 'ay'
