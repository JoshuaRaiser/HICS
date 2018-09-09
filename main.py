import matplotlib.pyplot as plt
import numpy as np
import random
import math

from objects.ion import Ion
from mathematics.calculator import Calculate

# list of coordinates of the nucleons for each ion
positions_xy_right_ion = []
positions_xy_left_ion = []
impact_param = 0

def main():
    # define global vars to use in this scope
    global positions_xy_left_ion, positions_xy_right_ion, impact_param

    # the right ion on collision
    right_ion = Ion()
    right_ion.define_gold_ion()

    # the left ion on collision
    left_ion = Ion()
    left_ion.define_gold_ion()

    # initialize lists of the ion's nucleons coordinates
    positions_xy_right_ion = initialize_nucleon_list(right_ion, 0)
    positions_xy_left_ion = initialize_nucleon_list(left_ion, 1)

    # draw graph of coordinates lists
    impact_param = right_ion.R
    create_graph(positions_xy_left_ion, positions_xy_right_ion)

    plt.show()

def initialize_nucleon_list(ion, direction):
    xy_list = []
    for index in range(ion.atomMass):
        cal = Calculate()
        little_r = cal.calculate_nuclear_density(ion)[0]
        theta_angle = random.uniform(0, 2 * math.pi)
        pos_x = cal.calculate_x(little_r, theta_angle, direction)
        pos_y = cal.calculate_y(little_r, theta_angle)
        xy_list.append([pos_x, pos_y])
    return xy_list

def create_graph(left, right):
    plt.figure(1)
    plt.title("nuclear collision")
    for index in range(len(left)):
        plt.scatter(left[index][0], left[index][1], s=80, facecolors='none', edgecolors='b')
    for index in range(len(right)):
        plt.scatter(right[index][0], right[index][1], s=80, facecolors='none', edgecolors='r')
    x_axis = np.linspace(-impact_param, impact_param)  # onde começa e onde termina o eixo X
    y_axis = np.linspace(-impact_param, impact_param)  # onde começa e onde termina o eixo Y
    X, Y = np.meshgrid(x_axis*2, y_axis*2)
    F1 = (X - impact_param / 2) ** 2 + Y ** 2 - impact_param ** 2
    F2 = (X + impact_param / 2) ** 2 + Y ** 2 - impact_param ** 2
    plt.contour(X, Y, F1, [0], colors='b')
    plt.contour(X, Y, F2, [0], colors='r')
    plt.axis('equal')

if __name__ == "__main__":
    main()
