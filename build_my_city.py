# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:40:12 2016

@author: pi
"""

#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import time as t
import csv
import random
#Set the location of your 3D design file
file_path = '/home/pi/ava/hello_py/AvasMinecraftCity.csv'
post_to_chat = False
drift_rate = 0
# Connect to minecraft
mc = minecraft.Minecraft.create()
mc.postToChat('Hi, its Ava and I''m going to build a city')


pos = mc.player.getPos() #get current position
starting_spot = {}
starting_spot['x'] = pos.x
starting_spot['y']= pos.y
starting_spot['z']= pos.z
    #moves -20-20 steps forward/bakcwards
#starting_spot['x'] = pos.x + random.randint(-drift_rate,drift_rate)
starting_spot['y']= pos.y
     #moves -20-20 steps forward/bakcwards
#starting_spot['z']= pos.z  + random.randint(-drift_rate,drift_rate)   
    #teleport player to new position
#mc.player.setTilePos(starting_spot['x'],starting_spot['y']+5,starting_spot['z'])#
#mc.postToChat("Teleporting to %d, %d, %d"%(starting_spot['x']+5,starting_spot['y'],starting_spot['z']))
while True: #loop forever
#    pos = mc.player.getPos() #get current position
#    starting_spot['x'] = pos.x
#    starting_spot['y']= pos.y
#    starting_spot['z']= pos.z
    t.sleep(30)    
    row_count = 0
    column_count = 0
    layer_count = 0      
    #t.sleep(20)      
    print "opening file %s" %(file_path)      
    with open(file_path, 'rb') as f:
        print 'file opened'        
        reader = csv.reader(f)
        for row in reader:
            print row
            if 'layer' in row:
                layer_count+=1
                row_count = 0
                column_count = 0
                continue
                pass            
            
            row_count +=1
            for the_block in row:
                print the_block            
                if the_block == '' or ' ' in the_block :
                    print "use air"
                    the_block = 0
                #if the_block == 0:
                #    column_count +=1
                #    continue
                
                print "Placing block: %d, %d, %d" %(int(starting_spot['x'] + column_count), int(starting_spot['y']+layer_count),  int(starting_spot['z']+ row_count))
                mc.setBlock(int(starting_spot['x'] + column_count),int(starting_spot['y']+layer_count), int(starting_spot['z']+ row_count) , int(the_block), 1)
                #mc.postToChat("Placing block: %d, %d, %d" %(int(starting_spot['x'] + column_count), int(starting_spot['y']+layer_count),  int(starting_spot['z']+ row_count)))    
                column_count +=1
                #t.sleep(0.1)
            if post_to_chat:  
                mc.postToChat("Row completed, rc=%d cc=%d lc=%d" %(row_count, column_count, layer_count))
            column_count = 0
            t.sleep(.1)
    #Example of setting blocks
    #mc.setBlock(x + centre - r, int(y), z, block.TNT.id, 1)