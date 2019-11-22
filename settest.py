#!/usr/bin/env python3
#_*_coding:utf-8_*_

import sys
set_test = set()
for arg in sys.argv[1:]:
    #if len(arg) > 3:
    	set_test.add(arg)
print(' '.join(set_test))

