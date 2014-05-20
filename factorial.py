#!/usr/bin/env python

def factorial(n) :
	if n in (0,1) :
		return 1
	return n * factorial(n-1)

for i in range(10) :
	print factorial(i)
