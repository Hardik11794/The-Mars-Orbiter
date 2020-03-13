import pygame as pg
import os
import sys
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)





    

class Satellite(pg.sprite.Sprite):


    def __init__(self,background):

        super().__init__()
        self.screen = screen
        self.sat_image = pg.image.load("Images/Satellite.png").convert()
        self.sat_burn = pg.image.load("Images/Burn_Sat.png").convert()
        self.image = self.sat_image
        
        self.rect = self.sat_image.get_rect()
        self.screen_rect = screen.get_rect()
        
       

        self.x = random.randrange(315,425)
        self.y = random.randrange(70,180)
        self.dx = random.choice([-3,3])
        self.dy = 0

        self.heading = 0
        self.fuel = 0
        self.mass = 1
        self.distance = 0
        self.thrust = pygame.mixer.Sound('Sound/Thrust_sound.wav')
        self.thrust.set_volume(0.07)

        
    def blitme(self):
        self.screen.blit(self.sat_image,self.rect)


screen_width = 1920
screen_height = 900
screen = pg.display.set_mode((screen_width,screen_height))

def run_simulation():
    pg.init()

    Satellite1 = Satellite(screen)

    

    while True:

        Satellite1.blitme()
        pg.display.update()  


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    #pg.display.flip()

run_simulation()

