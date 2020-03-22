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

def calc_eccentricity(dist_list):
    """Calc and return eccentricity from the list of radii"""
    apoapsis = max(dist_list)
    periapsis = min(dist_list)

    eccentricity = (apoapsis - periapsis)/(apoapsis + periapsis)
    
    return eccentricity

def instruct_label(screen,text,color,x,y):

    """take a screen,list of strings,color and origin & render text to screen"""
    instruct_font = pg.font.SysFont(None, 22)
    line_spacing = 22
    for index,line in enumerate(text):
        label = instruct_font.render(line,True,color,BLACK)
        screen.blit(label,(x,y + index * line_spacing))
        
def box_label(screen,text,dimensions):
    
    """Make a fixed size label from screen,text & left,top,width,height"""

    readout_font = pg.font.SysFont(None,22)
    base = pg.Rect(dimensions)
    pg.draw.rect(screen,WHITE,base,0)
    label = readout_font.render(text,True,BLACK)
    label_rect = label.get_rect(center = base.center)
    screen.blit(label,label_rect)

def mapping_on(planet):
    """Show soil moisture images of planet"""
    last_center = planet.rect.center
    planet.image_copy = pg.trasform.scale(planet.image_water,(100,100))
    planet.image_copy.set_colorkey(BLACK)
    planet.rect = planet.image_copy.get_recct()
    planet.rect.center = last_center

def mapping_off(planet):

    """Restore normal planet image"""
    planet.image_copy = pg.transform.scale(planet.image_mars,(100,100))
    planet.image_copy.set_colorkey(BLACK)

def cast_shadow(screen):
    """Add optional terminator & shadow behind planet to screen"""

    shadow = pg.Surface((400,100),flags=pg.SRCALPHA)
    shadow.fill((0,0,0,210))  #last number sets 
    screen.blit(shadow,(0,270)) #tuple is top left coordinates