#!/usr/bin/python3


a, b = map(int, input().split())


print(id(a), id(b))


a, b = b, a
print(a, b)
print(id(a), id(b))




a, b = b, a 
temp = a
a = b 
b = temp
print(a, b)





