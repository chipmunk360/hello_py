# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 21:47:23 2016

@author: 
"""

import pygame, sys, random
skier_images = ['skier_down.png', 'skier_right1.png',
                'skier_right2.png', 'skier_left2.png',
                'skier left1.png']
                
class SkierClass (pygame.sprite.Sprite):
    def _init_(self):
        (pygame.sprite.sprite.Sprite) :
            self.image = pygame.image.load("skier_down.png")
            self.rect = self.image.get.rect()
            self.rect.center = [320, 100]
            self.angle = 0
        
        
def turn (self, direct):
    self.angle = self.angle + direction
    
        
                   