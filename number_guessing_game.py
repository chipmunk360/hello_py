# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:29:02 2016

@author: pi
"""

import random
secret = random.randint ( 1, 20)
guess = 0
tries = 0
print "AHOY! i'm  the Dread Pirate Roberts and I hae a secret!" 
print " It is a number from 1 to 20. I'll give you 6 tries. "

while guess  != secret  and tries < 6:
   
    guess = input ( 'whats yer guees')
#==============================================================================
#     print "guess: %s secret: %s tries: %s" %(guess, secret, tries)
#==============================================================================
    if guess < secret:
        print" too low ye scurvy dog."
    elif guess > secret:
        print "too high landlubber!"
    tries = tries + 1
    
    
if guess == secret:
    '''they guessed correctly'''
    print "Avast! Ye got it! Found my secret ye did!"
else:
    print "No More guesses! Better luck next time, matey!"
    print "The secret number was ", secret
    
        