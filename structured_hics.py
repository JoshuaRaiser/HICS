# imports
import math
import random
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec

# from archive dot py imports
from objects.ion import Ion

# error messages
ERROR_INVALID_DIRECTION_MESSAGE = 'Invalid direction error.'

# directions
RIGHT = 0
LEFT = 1

# non constants global vars
impact_parameter = 0
impact_parameter_list = []

# constants vars
a_em = 1/137
proton_radius = 0.84    # 0.84 - 0.87
vn = math.sqrt(1 - ((2*938.272046)/200000)**2)

# create 2x2 sub plots
gd = gridspec.GridSpec(2, 2, wspace=0.4, hspace=0.3)
plt.figure()

def main():
    global impact_parameter, impact_parameter_list

    # ions in collision
    ion = Ion()
    ion.define_gold_ion()

    # vars list
    impact_parameter_limit = 14
    for_count = 1000

    # ion's nucleons coordinates list
    nucleons_positions_xy_right_ion = []
    nucleons_positions_xy_left_ion = []

    # electromagnetic field event results
    eEx_event = []
    eEy_event = []
    eBx_event = []
    eBy_event = []
    eBy_event_nomodule = []

    while impact_parameter <= impact_parameter_limit:
        eEx_sum, eEy_sum = 0, 0
        eBx_sum, eBy_sum = 0, 0
        eBy_sum_raw = 0

        for index in range(for_count):

            nucleons_positions_xy_right_ion = initialize_nucleons_list(ion, RIGHT)
            nucleons_positions_xy_left_ion = initialize_nucleons_list(ion, LEFT)

            # calculate the electric field
            eExy_right = electric_field(nucleons_positions_xy_right_ion, RIGHT)
            eExy_left = electric_field(nucleons_positions_xy_left_ion, LEFT)
            eEx_sum += math.fabs(eExy_right[0] + eExy_left[0])
            eEy_sum += math.fabs(eExy_right[1] + eExy_left[1])

            # calculate the magnetic field
            eBxy_right = magnetic_field(nucleons_positions_xy_right_ion, RIGHT)
            eBxy_left = magnetic_field(nucleons_positions_xy_left_ion, LEFT)
            eBx_sum += math.fabs(eBxy_right[0] + eBxy_left[0])
            eBy_sum += math.fabs(eBxy_right[1] + eBxy_left[1])
            eBy_sum_raw += eBxy_right[1] + eBxy_left[1]

        # calculate the events and add to the respective event list
        eEx_event.append(eEx_sum/for_count)
        eEy_event.append(eEy_sum/for_count)
        eBx_event.append(eBx_sum/for_count)
        eBy_event.append(eBy_sum/for_count)
        eBy_event_nomodule.append(eBy_sum_raw/for_count)

        #print('Ex esquerda: ' + str(eEx_left_sum/for_count) + ' Ex direita: ' + str(eEx_right_sum/for_count))

        impact_parameter_list.append(impact_parameter)
        impact_parameter += 2

    # plot graphs
    create_ion_graph(nucleons_positions_xy_right_ion, nucleons_positions_xy_left_ion, ion)
    create_magnetic_field_graph(eBx_event, eBy_event, eBy_event_nomodule)
    create_electric_field_graph(eEx_event, eEy_event)
    plt.show()

def initialize_nucleons_list(ion, direction):
    xy_nucleons_list = []
    pos_x = 0
    pos_y = 0

    for index in range(ion.atom_num):
        r = random.uniform(0, ion.R)
        theta_angle = random.uniform(0, 2*math.pi)

        if direction == RIGHT:
            pos_x = r * math.cos(theta_angle) + impact_parameter/2

        elif direction == LEFT:
            pos_x = r * math.cos(theta_angle) - impact_parameter/2

        else:
            raise ValueError(ERROR_INVALID_DIRECTION_MESSAGE)

        pos_y = r * math.sin(theta_angle)
        xy_nucleons_list.append([pos_x, pos_y])

    return xy_nucleons_list

def electric_field(nucleon_list, direction):
    sum_x, sum_y = 0, 0

    for index in range(len(nucleon_list)):
        x = nucleon_list[index][0]
        y = nucleon_list[index][1]

        if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:

            if direction == RIGHT or direction == LEFT:
                rn = math.sqrt(x ** 2 + y ** 2)
                sum_x += x / (rn ** 3)
                sum_y += y / (rn ** 3)

    e_x = a_em / math.sqrt(1 - (vn ** 2)) * sum_x
    e_y = a_em / math.sqrt(1 - (vn ** 2)) * sum_y
    return [e_x, e_y]

def magnetic_field(nucleon_list, direction):
    sum_x, sum_y = 0, 0

    for index in range(len(nucleon_list)):
        x = nucleon_list[index][0]
        y = nucleon_list[index][1]

        if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
            rn = math.sqrt(x ** 2 + y ** 2)

            if direction == RIGHT:
                sum_x += -y / (rn ** 3)
                sum_y += x / (rn ** 3)

            elif direction == LEFT:
                sum_x += y / (rn ** 3)
                sum_y += -x / (rn ** 3)

            else:
                raise ValueError(ERROR_INVALID_DIRECTION_MESSAGE)

    e_x = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_x
    e_y = (a_em * vn) / math.sqrt(1 - (vn ** 2)) * sum_y
    return [e_x, e_y]

def create_ion_graph(left, right, ion):
    global gd
    # row 0, span all columns
    ax = plt.subplot(gd[0, :])
    plt.axis('equal')
    plt.title("Heavy Ion Collision Simulator  A+A (" + ion.symbol + ")")

    # draw ion's nucleons
    for index in range(ion.atom_num):
        plt.scatter(right[index][0], right[index][1], s=100, facecolors='none', edgecolors='b')

    for index in range(ion.atom_num):
        plt.scatter(left[index][0], left[index][1], s=100, facecolors='none', edgecolors='r')

    # draw ions
    gca = plt.gca()
    gca.add_patch(plt.Circle((-impact_parameter / 2, 0), radius=ion.R, facecolor='none', edgecolor='b'))
    gca.add_patch(plt.Circle((impact_parameter / 2, 0), radius=ion.R, facecolor='none', edgecolor='r'))

    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])

def create_magnetic_field_graph(magnetic_field_x_event, magnetic_field_y_event, magnetic_field_y_event_nomodule):
    global gd
    # row 1, column 0
    plt.subplot(gd[1, 0])
    plt.title("Magnetic Field (B)")
    plt.xlabel("b (fm)")
    plt.ylabel("e.B Field event")

    plt.plot(impact_parameter_list, magnetic_field_x_event, 'bo-', label='|B(x)|')
    plt.plot(impact_parameter_list, magnetic_field_y_event, 'r.-', label='|B(y)|')
    plt.plot(impact_parameter_list, magnetic_field_y_event_nomodule, 'k^-', label='B(y)')
    plt.legend(loc='upper right', borderaxespad=0.1)

def create_electric_field_graph(electric_field_x_event, electric_field_y_event):
    global gd
    # row 1, column 1
    plt.subplot(gd[1, 1])
    plt.title("Electric Field (E)")
    plt.xlabel("b (fm)")
    plt.ylabel("e.E Field event")

    plt.plot(impact_parameter_list, electric_field_x_event, 'bo-', label='|E(x)|')
    plt.plot(impact_parameter_list, electric_field_y_event, 'r.-', label='|E(y)|')
    plt.legend(loc='upper right', borderaxespad=0.1)

if __name__ == "__main__":
    main()
