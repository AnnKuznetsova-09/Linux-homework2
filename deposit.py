#!/usr/bin/env python3



import sys


principal = float(sys.argv) 
rate = float(sys.argv) / 100 
years = int(sys.argv) 


amount = principal * ((1 + rate) ** years) 
print(f"{amount:.2f}")
