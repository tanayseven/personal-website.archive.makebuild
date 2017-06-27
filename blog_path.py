#!/usr/bin/env python3
import sys
str_lst = sys.argv[1].split('-')
result = str_lst[0]+'/'+str_lst[1]+'/'+str_lst[2]+'/'+'-'.join(str_lst[3:])
print(result)