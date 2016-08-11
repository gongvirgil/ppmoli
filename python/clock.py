#!/usr/bin/env python
# -* - coding: UTF-8 -* -
#
#
# show time in console
#
import time

while True:
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    print t
    time.sleep(1)
