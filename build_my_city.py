# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:40:12 2016

@author: pi
"""

#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import time
# Connect to minecraft
mc = minecraft.Minecraft.create()
mc.postToChat('Hi, its Ava and I''m going to buils a city')

starting_spot = {}
starting_spot['x'] = -51
starting_spot['y']= -120
starting_spot['z']= 18

