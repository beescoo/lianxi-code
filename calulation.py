#!usr/bin/env python3

a = 0
while a <= 100:
	a = a + 1
	b = (1 + a) * a // 2 + a // 2 * a % 2
	if a == 100:
	    print('The sum is {}'.format(b))