#!/usr/bin/env python
# -* - coding: UTF-8 -* -

# 判断是否是回文的函数（函数之前空两行）


def isPalindrome(str):
    if len(str) <= 1:
        return True
    p = len(str) - 1
    if str[p] == str[0]:
        return isPalindrome(str[1:p])
    else:
        return False

print u"------判断是否为回文------".encode("GBK")
str = raw_input(u"请输入字符串:".encode("GBK"))
if len(str) < 1:
    str = raw_input(u"输入为空，请重新输入字符串:".encode("GBK"))
if isPalindrome(str):
    print str, u"是回文".encode("GBK")
else:
    print str, u"不是回文".encode("GBK")
