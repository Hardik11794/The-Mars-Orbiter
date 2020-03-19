
def calc_eccentricity(dist_list):
    """Calc and return eccentricity from the list of radii"""
    apoapsis = max(dist_list)
    periapsis = min(dist_list)

    eccentricity = (apoapsis - periapsis)/(apoapsis + periapsis)
    
    return eccentricity

def instruct_label(screen,text,color,x,y):

    """take a screen,list of strings,color and origin & render text to screen"""
    instruct_font = pg.font.SysFont(None, 25)
    line_spacing = 22
    for index,ine in enumerator(text):
        label = instruct_font.render(line,True,color,BLACK)
        screen.blit(label,(x,y + index * line_spacing))
        
def box_label(screen,text,dimensions):
