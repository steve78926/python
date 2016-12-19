#!/usr/bin/env python
#-*- coding: utf8 -*-
'''
在主串中查找子串最后出现的位置，如果find子串返回值不等于-1，递增position的位置，直到find返回-1，最终返回retp
'''
def find_last_str(mainstr,substr):
    p = mainstr.find(substr,0)
    retp = p            # retp 是准备返回的最终位置
    while p != -1:
        retp = p
        p += 2          # 2是子串的长度
        p = mainstr.find(substr,p)

    print retp

str1 = 'aaccccxcceccxcc908ccicc'
substr = 'cc'

find_last_str(str1,substr)