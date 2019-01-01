# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/pi/.spyder2/.temp.py
"""

def dad_is_annoying(name):
    '''This is why I know he loves me'''
    print "%s have you done your reading log?\n" %(name)

def empathy_for_bad_day(how_was_day, name):
    
    if how_was_day == "bad":
        print "lol what a loser sux for u %s" %(name)
    else:
        print "That's nice %s" %(name)

def favorite_color_praise(name, fav_color):
    print "Oh, I like %s %s" %(fav_color,name)
    
    

#print "i love pizzia"
#print "pizza"*20
#print "yum"*40
#print "i'm full"

while True:
    #name = ""


    print "hello what's your name"
    name = raw_input ("What is your name?")
    
    if name == "stop":
        break
    print "Answer: %s" %(name)
    print "that is a nice name %s" %(name)
    
    how_was_day = raw_input("How was your day %s" %(name))
     
    empathy_for_bad_day(how_was_day, name)

    dad_is_annoying(name)
    fav_color = raw_input("whats your favorite color?")
    
    favorite_color_praise(name, fav_color)
    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 




