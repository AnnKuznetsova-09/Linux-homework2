#!/usr/bin/python3



s = input()

length = len(s)
first = s
last = s[-1]
mid = s[len(s)//2]
every_second = s[::2]
reversed_s = s[::-1]
is_palindrome = s == s[::-1]


print(length, first, last, mid, every_second, reversed_s, is_palindrome)
