import pygame as pg
import os
import sys
import random
import math
from Modules import Satellite
from Modules import Planet
from Modules import Game_Functions as gf

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
LT_BLUE = (173,216,230)


def main():
    """set up labels & instructions,crate objects & run the game loop"""
    pg.init()  #initialize pygame

    #Set up display:
    os.environ["SDL_VIDEO_WINDOWS_POS"] = '700,100' #Set the game window origin
    screen = pg.display.set_mode((800,645),pg.FULLSCREEN)
    pg.display.set_caption("Mars Orbiter")
    background = pg.Surface(screen.get_size())

    pg.mixer.init() #For sound effect

    intro_text = [
        'The Mars Orbiter experienced an error during Orbit insertion.',
        'Use thrusters to coreect to circular mapping orbit without',
        'running out of propellant or burning up in atmosphere.'
        ]

    instruct_text1 = [
        'Orbital altitude must be within 69-120 miles.',
        'Orbital Eccentricity must be < 0.05',
        'Avoid top of atmosphere at 68 miles'
        ]

    instruct_text2 = [
        'Left Arrow = Decrease Dx',
        'Right Arrow = Increase Dx',
        'Up Arrow =  Decrease Dy',
        'Down Arrow = Increase Dy',
        'Space Bar = Clear Path',
        'Escape = Exit Full Screen'
        ]

    planet = Planet.Planet()
    planet_sprite = pg.sprite.Group(planet)
    sat = Satellite.Satellite(background)
    sat_sprite = pg.sprite.Group(sat)

    #for circular orbit verification
    dist_list = []
    eccentricity = 1
    eccentricity_calc_interval = 5 #optiomizes for 120 mile altitude

    #time keeping
    clock = pg.time.Clock()
    fps = 30
    tick_count = 0

    #for soil moisture mapping functionality
    mapping_enabled = False

    running = True
    while running:
        clock.tick(fps)
        tick_count += 1
        dist_list.append(sat.distance)

        #get keyboard input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                screen = pg.display.set_mode((800,645)) #Exit full screen
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                background.fill(BLACK) # clear path
            elif event.type == pg.KEYUP:
                sat.thrust.stop() #Stop sound
                gf.mapping_off(planet) #turn off moisture map view
            elif mapping_enabled:
                if event.type == pg.KEYDOWN and event.key == pg.K_m:
                    gf.mapping_on(planet)

                #Get heading & distance to planet & apply gravity
            sat.locate(planet)
            planet.gravity(sat)

                #calculate orbital eccentricity
            if tick_count % (eccentricity_calc_interval * fps) == 0:
                eccentricity = gf.calc_eccentricity(dist_list)
                dist_list = []

                #re-blit background for drawing command-prevents clearing path
            screen.blit(background,(0,0))

                #Fuel/Altitude fail conditions
            if sat.fuel <= 0:
               gf.instruct_label(screen,['Fuel Depleted!'],RED,340,195)
               sat.fuel = 0
               sat.dx = 2

            elif sat.distance <= 68:
                 gf.instruct_label(screen,['Atmospheric Entry!'],RED,320,195)
                 sat.fuel = 0
                 sat.dx = 0

            if eccentricity < 0.05 and sat.distance >= 69 and sat.distance <= 120:
                map_instruct = ['Press & Hold M to map soil moisture']
                gf.instruct_label(screen,map_instruct,LT_BLUE,250,175)
                mapping_enabled = True

            else:
                mapping_enabled = False

            planet_sprite.update()
            planet_sprite.draw(screen)
            sat_sprite.update()
            sat_sprite.draw(screen)
                
            #display intro text for 15 seconds
            if pg.time.get_ticks() <= 5000: #time in milliseconds
                gf.instruct_label(screen,intro_text,GREEN,145,100)

            #display telemetry and instructions
            gf.box_label(screen,'Dx',(70,20,75,20))
            gf.box_label(screen,'Dy',(150,20,80,20))
            gf.box_label(screen,'Altitude',(240,20,160,20))
            gf.box_label(screen,'Fuel',(410,20,160,20))
            gf.box_label(screen,'Eccentricity',(580,20,150,20))

            gf.box_label(screen,'{:.1f}'.format(sat.dx),(70,50,75,20))
            gf.box_label(screen,'{:.1f}'.format(sat.dy),(150,50,80,20))
            gf.box_label(screen,'{:.1f}'.format(sat.distance),(240,50,160,20))
            gf.box_label(screen,'{}'.format(sat.fuel),(410,50,160,20))
            gf.box_label(screen,'{:8f}'.format(eccentricity),(580,50,150,20))



            gf.instruct_label(screen,instruct_text1,WHITE,10,575)
            gf.instruct_label(screen,instruct_text2,WHITE,570,510)

            #add terminator & border
            gf.cast_shadow(screen)
            pg.draw.rect(screen,WHITE,(1,1,798,643),1)

            pg.display.flip()

        
   #if __name__=="__main__":
main()

















































