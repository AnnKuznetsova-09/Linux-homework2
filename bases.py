#!/usr/bin/python3


import sys
n = int(sys.argv)

bin_str = bin(n)
oct_str = oct(n)
hex_str = hex(n)


n_from_bin = int(bin_str, 2)
n_from_oct = int(oct_str, 8)
n_from_hex = int(hex_str, 16)


print(bin_str, oct_str, hex_str)
