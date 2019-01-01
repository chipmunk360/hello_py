# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 02:32:20 2016

@author: pi
"""

print 5

"""This is something"""
'''This is something'''

print 1234567898765432123456789 * 9876543212345678987654321
print "cat" + "dog"
print "Hello" * 20
print "I love pizza!"
print "pizza" * 20
print "yum" * 40
print "I'm full."

import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."

while guess != secret and tries < 6:
    guess = input("What's yer guess? ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
        print " Too high, landlubber!"
    tries = tries + 1