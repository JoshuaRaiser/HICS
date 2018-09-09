import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import random
import math

from objects.ion import Ion
from mathematics.calculator import Calculator

# list of coordinates of the nucleons for each ion
positions_xy_right_ion = []
positions_xy_left_ion = []
impact_param = 0

def main():
    # define global vars to use in this scope
    global positions_xy_left_ion, positions_xy_right_ion, impact_param
    # Todo: this parameter must be choose by user
    impact_param = 5

    # the right ion on collision
    right_ion = Ion()
    right_ion.define_copper_ion()

    # the left ion on collision
    left_ion = Ion()
    left_ion.define_copper_ion()

    # initialize lists of the ion's nucleons coordinates
    positions_xy_right_ion = initialize_nucleon_list(right_ion, 0)
    positions_xy_left_ion = initialize_nucleon_list(left_ion, 1)

    # draw graph of coordinates lists
    ion_radius = right_ion.R
    create_ion_graphs(positions_xy_left_ion, positions_xy_right_ion, ion_radius)

    # show the graph
    plt.title("Heavy Ion Collision Simulator (" + left_ion.symbol + " + " + right_ion.symbol + ")")
    plt.show()

def initialize_nucleon_list(ion, direction):
    xy_list = []
    for index in range(ion.atomMass):
        cal = Calculator()
        little_r = cal.calculate_nuclear_density(ion, impact_param)[0]
        theta_angle = random.uniform(0, 2 * math.pi)
        pos_x = cal.calculate_x(little_r, theta_angle, direction)
        pos_y = cal.calculate_y(little_r, theta_angle)
        xy_list.append([pos_x, pos_y])
    return xy_list

def create_ion_graphs(left, right, ion_radius):
    plt.figure(1)
    # draw the nucleons
    for index in range(len(left)):
        plt.scatter(left[index][0], left[index][1], s=80, facecolors='none', edgecolors='b')
    for index in range(len(right)):
        plt.scatter(right[index][0], right[index][1], s=80, facecolors='none', edgecolors='r')
    # draw the circles to represent the Ions
    ax = plt.gca()
    ax.add_patch(plt.Circle((impact_param/2, 0), radius=ion_radius, facecolor='none', edgecolor='b'))
    ax.add_patch(plt.Circle((-impact_param/2, 0), radius=ion_radius, facecolor='none', edgecolor='r'))
    plt.axis('equal')

if __name__ == "__main__":
    main()
