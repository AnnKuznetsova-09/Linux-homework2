#!/usr/bin/python3


n = int(input())


digit_sum = (n // 100) + (( n // 10) % 10) + (n % 10)
reversed_arith = (n % 10) * 100 + (( n // 10) % 10) * 10 + (n // 100)
reversed_slice = int(str(n)[::-1])

print(digit_sum, reversed_slice)
