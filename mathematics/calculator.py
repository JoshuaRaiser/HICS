import random
import math

from scipy.optimize import fsolve
from objects.ion import Ion

class Calculator:

    # these global variables are used to setup the direction from which the ions originates
    DIRECTION_RIGHT = 1
    DIRECTION_LEFT = 0

    '''
    ' @Constructor
    ' this is the constructor method for this class
    '''
    def __init__(self):
        self.w = 0                                          # the parameter w of the 3pF and 3pG models
        self.po = 1                                         # initial nuclear density
        self.p = random.uniform(0, 1)                       # final nuclear density, random number (0 < p < 1)
        self.F = random.uniform(0, 1)                       # a random number between 0 and 1 (0 < F < 1)
        self.actual_ion = Ion()                             # just the actual Ion type(objects/ion.py)
        self.impact_param = 0.0                             # parameter of the impact of the collision

        # constants to electromagnetic field
        self.proton_radius = 0.84                           # proton radius to avoid division by zero (0.84 - 0.87)
        self.a_em = 1/137.03599911                          # constant of fine structure
        self.va_2 = math.fabs(1 - ((2*938.272046)/200)**2)  # magnitude of velocity, determined by collision energy (RHIC = 200 MeV)
                                                            # and the proton mass = 938.272046 MeV

    '''
    ' @Calculate
    ' this functions calculate the nuclear density (r)
    ' entries -> Ion type(objects/ion.py)
    ' exit -> nuclear density (float)
    '''
    def calculate_nuclear_density(self, ion, b):
        self.actual_ion = ion
        self.impact_param = b
        return fsolve(self.__calculate_find_root_integrated, 0.0)

    '''
    ' @Calculate
    ' this function calculate the x position of nucleon into the ion
    ' entries -> nd (nuclear density (float)), theta_angle (float)
    ' exit -> x (float)
    '''
    def calculate_x(self, nd, theta_angle, direction):
        if direction == Calculator.DIRECTION_RIGHT:
            return ((nd * math.cos(theta_angle))) + self.impact_param / 2
        elif direction == Calculator.DIRECTION_LEFT:
            return ((nd * math.cos(theta_angle))) - self.impact_param / 2
        else:
            raise ValueError("The value of direction must be 1 for RIGHT or 0 for LEFT. (calculator.py>calculate_x)")

    '''
    ' @Calculate
    ' this function calculate the y position of nucleon into the ion
    ' entries -> nd (nuclear density (float)), theta_angle (float)
    ' exit -> y (float)
    '''
    def calculate_y(self, nd, theta_angle):
        return (nd * math.sin(theta_angle))

    '''
    ' @Calculate
    ' this function calculate the X of function already integrated (when w is 0)
    '
    '   Integrate
    '   / r
    '   |    (1 / (1 + e^((r - R) / a))) * dr , where r = x
    '   / 0
    '
    '   Integrated
    '   1 / R [ r - a * ln(e^(R/a) + e^(r/a)) + R] - F = 0,
    '   where F is a random number between 0 and 1: (0 < F < 1)
    '       
    ' entries -> x (float)
    ' exit -> next_x (float)
    '''
    def __calculate_find_root_integrated(self, x):
        # Todo: develop and integrate an equation to do a method when w is not 0
        ion = self.actual_ion
        next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - self.F
        return next_x

    '''
    ' @Calculate
    ' this function calculate the Electric Field of the collision (E)
    ' entries -> xy[[x, y]] (float)
    ' exit -> xy[x, y] (float), coordinates X and Y of one point to graph of Electric Field (E)
    '''
    def calculate_electric_field(self, xy_list):
        electric_field_x_list = []
        electric_field_y_list = []

        for xy in range(len(xy_list)):
            x = -xy_list[xy][0]
            y = -xy_list[xy][1]

            # to avoid division by zero, proceed only if X and Y are greater equal to proton radius
            if math.fabs(x) >= self.proton_radius and math.fabs(y) >= self.proton_radius:
                ra_module = math.sqrt(x**2 + y**2)
                e_x = self.__calculate_electric_field_equation(x, ra_module)
                e_y = self.__calculate_electric_field_equation(y, ra_module)
                electric_field_x_list.append(e_x)
                electric_field_y_list.append(e_y)

        x_electric_field = 0.0
        y_electric_field = 0.0
        for index in range(len(electric_field_x_list)):
            x_electric_field += math.fabs(electric_field_x_list[index])
            y_electric_field += math.fabs(electric_field_y_list[index])

        x_electric_field = self.a_em * x_electric_field
        y_electric_field = self.a_em * y_electric_field
        return [x_electric_field, y_electric_field]

    # Todo: do a comment to introduce at this method
    def __calculate_electric_field_equation(self, ra_vector_value, ra_module):
        dividend = (1 - self.va_2) * ra_vector_value
        divider = (ra_module**3) * ((1 - (ra_module * math.sqrt(self.va_2))**2)/(ra_module**2))**(3/2)
        return dividend / divider
