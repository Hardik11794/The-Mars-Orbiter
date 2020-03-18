
def calc_eccentricity(dist_list):
    """Calc and return eccentricity from the list of radii"""
    apoapsis = max(dist_list)
    periapsis = min(dist_list)

    eccentricity = (apoapsis - periapsis)/(apoapsis + periapsis)
    
    return eccentricity

