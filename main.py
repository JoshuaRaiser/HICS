import matplotlib.pyplot as plt

import random
import math

from objects.ion import Ion
from mathematics.calculator import Calculator

# impact parameter
impact_param = 0

# actual ion
ion = Ion()

def main():
    global impact_param, ion

    # list of electric and magnetic fields results
    electric_field_results = []
    magnetic_field_results = []

    # list of coordinates to electric field graph
    electric_field_coordinates = []
    magnetic_field_coordinates = []

    # list of coordinates of the nucleons for each ion
    positions_xy_right_ion = []
    positions_xy_left_ion = []

    while impact_param <= 12:
        sum_ex, sum_ey, sum_mx, sum_my, sum_my_nm = 0, 0, 0, 0, 0

        for index in range(100):
            # the right ion on collision
            right_ion = Ion()
            right_ion.define_gold_ion()

            # the left ion on collision
            left_ion = Ion()
            left_ion.define_gold_ion()

            # get actual
            ion = right_ion

            # initialize lists of the ion's nucleons coordinates
            positions_xy_right_ion = initialize_nucleon_list(right_ion, 0)
            positions_xy_left_ion = initialize_nucleon_list(left_ion, 1)

            # calculate the electric field of the collision
            cal = Calculator()
            electric_field_results.append(cal.calculate_electric_field(positions_xy_right_ion))
            electric_field_results.append(cal.calculate_electric_field(positions_xy_left_ion))

            # calculate the magnetic field of the collision
            magnetic_field_results.append(cal.calculate_magnetic_field(positions_xy_right_ion))
            magnetic_field_results.append(cal.calculate_magnetic_field(positions_xy_left_ion))

        for index in range(len(electric_field_results)):
            sum_ex += math.fabs(electric_field_results[index][0])
            sum_ey += math.fabs(electric_field_results[index][1])

            sum_mx += math.fabs(magnetic_field_results[index][0])
            sum_my += math.fabs(magnetic_field_results[index][1])

            # sum_my_nm += magnetic_field_results[index][1]

        # get the avg xy points to be the coordinates of electric and magnetic field at graph
        electric_field_coordinates.append([sum_ex/len(electric_field_results), sum_ey/len(electric_field_results)])
        magnetic_field_coordinates.append([sum_mx/len(magnetic_field_results), sum_my/len(magnetic_field_results)])
        electric_field_results = []

        impact_param += 2

    # draw graph of coordinates lists
    ion_radius = ion.R
    create_ion_graphs(positions_xy_left_ion, positions_xy_right_ion, ion_radius)
    #create_electric_field_graph(electric_field_coordinates)
    create_magnetic_field_graph(magnetic_field_coordinates)

    # show all graphs
    plt.subplots_adjust(hspace=0.5)
    plt.show()

def initialize_nucleon_list(ion, direction):
    xy_list = []

    for index in range(ion.atom_mass):
        cal = Calculator()
        little_r = cal.calculate_nuclear_density(ion, impact_param)[0]
        theta_angle = random.uniform(0, 2 * math.pi)
        pos_x = cal.calculate_x(little_r, theta_angle, direction)
        pos_y = cal.calculate_y(little_r, theta_angle)
        xy_list.append([pos_x, pos_y])

    return xy_list

def create_ion_graphs(left, right, ion_radius):
    plt.subplot(2, 1, 1)
    plt.title("Heavy Ion Collision Simulator (" + ion.symbol + " + " + ion.symbol + ")")

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

def create_electric_field_graph(electric_field_point_list):
    plt.subplot(2, 1, 2)
    plt.title("Electric Field")
    # plt.ylabel("(Electric Field)")
    # plt.xlabel("(b fm)")
    b_param = []
    ex_coordinates = []
    ey_coordinates = []
    count = 0

    for index in range(len(electric_field_point_list)):
        ex_coordinates.append(math.fabs(electric_field_point_list[index][0]))
        ey_coordinates.append(math.fabs(electric_field_point_list[index][1]))
        b_param.append(count)
        count += 2

    plt.plot(b_param, ex_coordinates, 'bo-', label='|E(x)|')
    plt.plot(b_param, ey_coordinates, 'r.-', label='|E(y)|')
    plt.legend(loc='upper right', borderaxespad=0.1)

def create_magnetic_field_graph(electric_field_point_list):
    plt.subplot(2, 1, 2)
    plt.title("Magnetic Field")
    # plt.ylabel("(Electric Field)")
    # plt.xlabel("(b fm)")
    b_param = []
    ex_coordinates = []
    ey_coordinates = []
    count = 0

    for index in range(len(electric_field_point_list)):
        ex_coordinates.append(math.fabs(electric_field_point_list[index][0]))
        ey_coordinates.append(math.fabs(electric_field_point_list[index][1]))
        b_param.append(count)
        count += 2

    plt.plot(b_param, ex_coordinates, 'bo-', label='|B(x)|')
    plt.plot(b_param, ey_coordinates, 'r.-', label='|B(y)|')
    plt.legend(loc='upper right', borderaxespad=0.1)

if __name__ == "__main__":
    main()
