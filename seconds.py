#!/usr/bin/python3
 
 s = int(input())
 hours, remainder = divmod(seconds, 3600)
 minutes, seconds = divmod(remainder, 60)
 
 print(f"{hours:02d}:{minutes:02d}:{second:02d}")

