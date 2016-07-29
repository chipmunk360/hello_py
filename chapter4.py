# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 01:14:00 2016

@author: pi
"""

a = 24
b = float(a)
print(a)
print(b)



c = 38.0
d = int(c)
print (c)
print(d)

e = 54.99
f = int(e)
print(e)
print(f)

a = '76.3'
b = float(a)
print (a)
print ("%0.8f"%(b))

a = '44.2'
b = 44.2
type(a)
type(b)
try:
    print float ("freD")
except Exception as e:
    print("Warning because of: %s"%(e))


fahr = 105
cel = 5.0 / 9 * (fahr - 32)
print("%0.2f degrees Fahrenheit is %0.2f degrees Celsius"%(fahr,cel))

