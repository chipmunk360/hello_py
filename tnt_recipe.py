
#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import time
# Connect to minecraft
mc = minecraft.Minecraft.create()
mc.postToChat('hi, its wyatt')

# Find out where we are in the world
playerPos = mc.player.getTilePos()
x = playerPos.x
# Our rainbow will be 5 blocks back from where we are standing
z = playerPos.z + 5
    
# Clean up the world and any previous rainbows
mc.setBlocks(x - 64, 1, z - 10, x + 64, 24, z + 10, block.AIR)
# Setup a grass floor
mc.setBlocks(x - 64, -2, z - 10, x + 64, 1, z + 10, block.GRASS.id)
height = 20
width = 20
centre = width / 2
while True:
    mc.postToChat('ready to begin constructiong a new TNT rainbow')
    for r in range(0, width):
        for colourindex in range(0, 6):
            mc.postToChat('setting block %d'%(colourindex))
            y = sin((r / float(width)) * pi) * height + colourindex
            mc.setBlock(x + centre - r, int(y), z, block.TNT.id, 1)

    mc.postToChat('The TNT rainbow has been completed sir, detonate when ready')
    time.sleep(30)
    mc.postToChat('Blow it up!')
    time.sleep(7)