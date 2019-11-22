#!/usr/bin/env python3

import sys
short_list,long_list = [],[]
for a in sys.argv[1:]:
    if len(a) < 3:
        short_list.append(a)
    else:
        long_list.append(a)
print(' '.join(short_list))
print(' '.join(long_list))