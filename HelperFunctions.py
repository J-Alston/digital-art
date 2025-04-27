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

class line_grid:
    '''
    Draws a grid of lines with angles and lengths corresponding to fields provided.
    theta_field and l_field are equally sized 2-d arrays.
    The lines are evenly distributed across the grid automatically.
    '''
    def __init__(self, theta_field, width, height):
        self.theta_field = theta_field
        self.width = width
        self.height = height

        shape = theta_field.shape
        
        l = 0.9*min([self.width, self.height])/max(shape)

        x_coords = np.linspace(0, width, len(theta_field[0]))
        y_coords = np.linspace(0, height, len(theta_field))

        self.line_grid = []

        for x, theta_row in zip(x_coords, theta_field):
            line_grid_row = []
            for y, theta in zip(y_coords, theta_row):
                line_grid_row.append(short_line(x, y, l, theta))

            self.line_grid.append(line_grid_row)
