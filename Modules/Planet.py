import pygame as pg
import os
import sys
import math

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
LT_BLUE = (173,216,230)


class Planet(pg.sprite.Sprite):

    """Planet object that rotates & projects gravity field"""

    def __init__(self):

        super().__init__()
        self.image_mars = pg.image.load("Images/mars.png").convert()
        self.image_water = pg.image.load("Images/mars_water.png").convert()
        self.image_copy = pg.transform.scale(self.image_mars,(100,100))
        self.image_copy.set_colorkey(BLACK)
        self.rect = self.image_copy.get_rect()
        self.image = self.image_copy
        self.mass = 2000
        self.x = 400
        self.y = 320
        self.rect.center=(self.x,self.y)
        self.angle = math.degrees(0)
        self.rotate_by = math.degrees(0.01)
    
    def rotate(self):
        """Rotate the planet image with each game loop"""

        last_center = self.rect.center
        self.image = pg.transform.rotate(self.image_copy,self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = last_center
        self.angle +=self.rotate_by

    def gravity(self,satellite):

        """Calculate the impact of gravity on satellite"""

        G =0.1
        dist_x = self.x - satellite.x
        dist_y = self.y - satellite.y
        distance = math.hypot(dist_x,dist_y)

        dist_x /= distance
        dist_y /= distance

        force = G * (satellite.mass * self.mass)/(math.pow(distance,2))
        satellite.dx += (dist_x * force)
        satellite.dy += (dist_y * force)
    
    def update(self):

        """Call rotating mathod"""

        self.rotate() 