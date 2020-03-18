import pygame as pg
import os
import sys
import random
import math
from Modules import Satellite
from Modules import Planet
from Modules import Game_Functions

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)





    



screen_width = 1920
screen_height = 900
screen = pg.display.set_mode((screen_width,screen_height))

def run_simulation():
    pg.init()

    Satellite1 = Satellite.Satellite(screen)

    

    while True:

        Satellite1.blitme()
        pg.display.update()  


        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    #pg.display.flip()

run_simulation()

