import pygame as pg
import os
import sys
import random
import math

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
LT_BLUE = (173,216,230)


class Satellite(pg.sprite.Sprite):


    def __init__(self,background):

        super().__init__()
        self.background = background
        self.sat_image = pg.transform.scale(pg.image.load("Images/Satellite.png").convert(),(40,40))
        self.sat_burn = pg.image.load("Images/Burn_Sat.png").convert()
        self.image = self.sat_image
        
        self.rect = self.sat_image.get_rect()
       # self.screen_rect = screen.get_rect()
        self.image.set_colorkey(BLACK) #sets transparent color        
       

        self.x = random.randrange(315,425)
        self.y = random.randrange(70,180)
        self.dx = random.choice([-3,3])
        self.dy = 0

        self.heading = 0
        self.fuel = 100
        self.mass = 1
        self.distance = 0
        self.thrust = pg.mixer.Sound('Sound/Thrust_sound.wav')
        self.thrust.set_volume(0.07)

        
    def blitme(self):
        self.screen.blit(self.sat_image,self.rect)

    def thruster(self,dx,dy):

        self.dx += dx
        self.dy += dy
        self.fuel -= 2
        self.thrust.play()

    def check_keys(self):

        keys=pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            self.thruster(dx=0.05,dy=0)
        elif keys[pg.K_LEFT]:
            self.thruster(dx=-0.05,dy=0)
        elif keys[pg.K_UP]:
            self.thruster(dx=-0,dy=-0.05)
        elif keys[pg.K_DOWN]:
            self.thruster(dx=-0,dy=0.05)

    def locate(self,planet):
        """Calculate the distance and heading to planet"""

        px,py = planet.x,planet.y
        dist_x = self.x - px
        dist_y = self.y - py

        #Get direction to planet to point to dish

        planet_dir_radians = math.atan2(dist_x,dist_y)
        self.heading =planet_dir_radians * 180/math.pi
        self.heading -= 90
        self.distance = math.hypot(dist_x,dist_y)

    def rotate(self):
        """Rotate the satellte using degress so dish faces planet"""
        self.image = pg.transform.rotate(self.sat_image,self.heading)
        self.rect =self.image.get_rect()

    def path(self):
        """Update the satellite position and draw line to trace orbital path"""
        last_center = (self.x,self.y)
        self.x += self.dx
        self.y += self.dy
        pg.draw.line(self.background,WHITE,last_center,(self.x,self.y))

    def update(self):

        """Update the satellite object during game"""
        self.check_keys()
        self.rotate()
        self.path()
        self.rect.center = (self.x,self.y)

        #change the image ti fiery red if in atmosphere
        if self.dx == 0 and self.dy == 0:
            self.image = self.image_crash
            self.image.set_colorkey(BLACK)





