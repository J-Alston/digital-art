import numpy as np

class short_line:
    def __init__(self, x, y, l, theta):
        '''
        Defines a line object centred on coords (x,y), with length l, and at an angle theta.
        '''
        self.x = x
        self.y = y
        self.l = l
        self.theta = theta

        x1 = self.x + self.l/2*np.cos(self.theta)
        y1 = self.y + self.l/2*np.sin(self.theta)
        x2 = self.x - self.l/2*np.cos(self.theta)
        y2 = self.y - self.l/2*np.sin(self.theta)

        self.xy = [(x1, y1), (x2, y2)]

def line_grid(theta_field, l_field):
    '''
    Draws a grid of lines with angles and lengths corresponding to fields provided.
    theta_field and l_field are equally sized 2-d arrays. 
    '''

    lg = short_line(theta_field, l_field)

    return lg