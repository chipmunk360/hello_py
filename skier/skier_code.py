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
        pygame.sprite.Sprite.__init__(self) 
            self.image = pygame.image.load("skier_down.png")
            self.rect = self.image.get.rect()
            self.rect.center = [320, 100]
            self.angle = 0
        
        
    def turn (self, direct):
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2:
        if self.angle > 2: self.angle = 2:
        center = self.rect.center
        self.image = pygame.image.load(skier_images{self.angle}
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6-abs(self.angle)*2]
        return speed
        
    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20: self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620            :
            
            
            
class ObstaclesClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, type):
        

    
        
                   