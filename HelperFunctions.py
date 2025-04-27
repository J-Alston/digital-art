import numpy as np

def short_line(x,y,l,theta):
    '''
    Defines a line object centred on coords (x,y), with length l, and at an angle theta.
    '''
    x1 = x + l/2*np.cos(theta)
    y1 = y + l/2*np.sin(theta)
    x2 = x - l/2*np.cos(theta)
    y2 = y - l/2*np.sin(theta)

    xy = [(x1, y1), (x2, y2)]

    return xy

def line_grid(theta_field, l_field):
    '''
    Draws a grid of lines with angles and lengths corresponding to fields provided.
    theta_field and l_field are equally sized 2-d arrays. 
    '''
