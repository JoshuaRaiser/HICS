# imports
import math
import random
import time
import configurations_hics
import matplotlib.pylab as plt
import matplotlib.gridspec as gridspec

# from archive dot py imports
from objects.ion import Ion
from scipy.optimize import fsolve

# error messages
ERROR_INVALID_DIRECTION_MESSAGE = 'Invalid direction error.'

# directions
RIGHT = 0
LEFT = 1

# non constants global vars
for_count = configurations_hics.config_for_count
impact_parameter = configurations_hics.config_impact_parameter
impact_parameter_limit = configurations_hics.config_impact_parameter_limit
impact_parameter_interval = configurations_hics.config_impact_parameter_interval

# list of the impact parameters who will be plot on graphs
impact_parameter_list = []

# non constants global vars to nuclear density
F = 0

# constants vars
a_em = 1/137            #
proton_radius = 0.84    # 0.84 - 0.87
vn = 0                  # unique constant modified by ion energy at collision

# create 2x2 subplots to results of collision
gd = gridspec.GridSpec(2, 2, wspace=0.4, hspace=0.3)
plt.figure(num='HICS - Heavy Ion Collision Simulator')

# electromagnetic field event results
eEx_event = []
eEy_event = []
eBx_event = []
eBy_event = []
eBy_event_nomodule = []

# create the ion
ion = Ion()

def main():
    print('Running...')
    global impact_parameter, impact_parameter_list
    global eEx_event, eEy_event, eBx_event, eBy_event, eBy_event_nomodule, vn, ion

    ion = configurations_hics.config_ion_type

    vn = math.sqrt(1 - ((2 * 938.272046) / (ion.gev*1000)) ** 2)

    # ion's nucleons coordinates list
    nucleons_positions_xy_right_ion = []
    nucleons_positions_xy_left_ion = []

    # standard deviation result error list
    bx_module_e = []
    by_module_e = []
    by_nomodule_e = []
    ex_module_e = []
    ey_module_e = []

    while impact_parameter <= impact_parameter_limit:
        eEx_sum, eEy_sum = 0, 0
        eBx_sum, eBy_sum = 0, 0
        eBy_sum_raw = 0
        sd_sum_Bx_module_2 = 0
        sd_sum_By_module_2 = 0
        sd_sum_By_nomodule_2 = 0
        sd_sum_Ex_module_2 = 0
        sd_sum_Ey_module_2 = 0

        for index in range(for_count):
            # print("Impact parameter: " + str(impact_parameter) + " /" + str(impact_parameter_limit) + " in for's index: " + str(index) + " /" + str(for_count))

            nucleons_positions_xy_right_ion = initialize_nucleons_list(RIGHT)
            nucleons_positions_xy_left_ion = initialize_nucleons_list(LEFT)

            # calculate the electric field
            eExy_right = electric_field(nucleons_positions_xy_right_ion)
            eExy_left = electric_field(nucleons_positions_xy_left_ion)
            eEx_sum += math.fabs(eExy_right[0] + eExy_left[0])
            eEy_sum += math.fabs(eExy_right[1] + eExy_left[1])

            # calculate the magnetic field
            eBxy_right = magnetic_field(nucleons_positions_xy_right_ion, RIGHT)
            eBxy_left = magnetic_field(nucleons_positions_xy_left_ion, LEFT)
            eBx_sum += math.fabs(eBxy_right[0] + eBxy_left[0])
            eBy_sum += math.fabs(eBxy_right[1] + eBxy_left[1])
            eBy_sum_raw += eBxy_right[1] + eBxy_left[1]

            # standard deviation
            sd_sum_Bx_module_2 += math.fabs(eBxy_right[0] + eBxy_left[0])**2
            sd_sum_By_module_2 += math.fabs(eBxy_right[1] + eBxy_left[1])**2
            sd_sum_By_nomodule_2 += (eBxy_right[1] + eBxy_left[1])**2
            sd_sum_Ex_module_2 += math.fabs(eExy_right[0] + eExy_left[0])**2
            sd_sum_Ey_module_2 += math.fabs(eExy_right[1] + eExy_left[1])**2

        # calculate the events and add to the respective event list
        eEx_event.append((eEx_sum/for_count))
        eEy_event.append((eEy_sum/for_count))
        eBx_event.append((eBx_sum/for_count))
        eBy_event.append((eBy_sum/for_count))
        eBy_event_nomodule.append((eBy_sum_raw/for_count))

        # calculate the standard deviation
        std = math.sqrt(math.fabs(sd_sum_Bx_module_2 / for_count - (eBx_sum/for_count)**2))               # sd.|Bx|
        bx_module_e.append(std)
        std = math.sqrt(math.fabs(sd_sum_By_module_2 / for_count - (eBy_sum / for_count) ** 2))         # sd.|By|
        by_module_e.append(std)
        std = math.sqrt(math.fabs(sd_sum_By_nomodule_2 / for_count - (eBy_sum_raw / for_count) ** 2))   # sd.By
        by_nomodule_e.append(std)
        std = math.sqrt(math.fabs(sd_sum_Ex_module_2 / for_count - (eEx_sum / for_count) ** 2))         # sd.|Ex|
        ex_module_e.append(std)
        std = math.sqrt(math.fabs(sd_sum_Ey_module_2 / for_count - (eEy_sum / for_count) ** 2))         # sd.|Ey|
        ey_module_e.append(std)

        impact_parameter_list.append(impact_parameter)
        impact_parameter += impact_parameter_interval

    # plot graphs
    create_ion_graph(nucleons_positions_xy_right_ion, nucleons_positions_xy_left_ion)
    create_magnetic_field_graph(eBx_event, eBy_event, eBy_event_nomodule)
    create_electric_field_graph(eEx_event, eEy_event)
    create_standard_deviation_graph(bx_module_e, by_module_e, by_nomodule_e, ex_module_e, ey_module_e)

def initialize_nucleons_list(direction):
    global F
    xy_nucleons_list = []
    pos_x = 0
    pos_y = 0

    for index in range(ion.atom_num):
        F = random.uniform(0, 1)
        r = fsolve(__calculate_find_root_integrated, 0.0)[0]
        theta_angle = random.uniform(0, 2*math.pi)

        if direction == RIGHT:
            pos_x = r * math.cos(theta_angle) + impact_parameter/2

        elif direction == LEFT:
            pos_x = r * math.cos(theta_angle) - impact_parameter/2

        else:
            raise ValueError(ERROR_INVALID_DIRECTION_MESSAGE)

        pos_y = r * math.sin(theta_angle)
       #print('x: '+str(pos_x)+' y: '+str(pos_y))
        xy_nucleons_list.append([pos_x, pos_y])

    return xy_nucleons_list

def __calculate_find_root_integrated(x):
    # Todo: develop and integrate an equation to do a method when w is not 0
    p0 = (1 / (ion.a * math.log(math.exp(ion.R / ion.a) + 1)))
    next_x = p0 * (x - ion.a * math.log((1 + math.exp((x - ion.R) / ion.a) / (1 + math.exp(-ion.R / ion.a))))) - F
    #next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - F
    return next_x

def electric_field(nucleon_list):
    sum_x, sum_y = 0, 0

    for index in range(len(nucleon_list)):
        x = nucleon_list[index][0]
        y = nucleon_list[index][1]

        #if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
        if math.sqrt(x ** 2 + y ** 2) >= proton_radius:

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

        #if math.fabs(x) >= proton_radius and math.fabs(y) >= proton_radius:
        if math.sqrt(x ** 2 + y ** 2) >= proton_radius:

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

def create_ion_graph(left, right):
    global gd
    # row 0, span all columns
    ax = plt.subplot(gd[0, :])
    plt.axis('equal')
    plt.title("Heavy Ion Collision Simulator  A+A (" + ion.symbol + ")")
    plt.xlabel("$x(fm)$")
    plt.ylabel("$y(fm)$")

    # draw ion's nucleons
    for index in range(ion.atom_num):
        plt.scatter(right[index][0], right[index][1], s=100, facecolors='none', edgecolors='b')

    for index in range(ion.atom_num):
        plt.scatter(left[index][0], left[index][1], s=100, facecolors='none', edgecolors='r')

    # draw ions
    gca = plt.gca()
    gca.add_patch(plt.Circle((-(impact_parameter - impact_parameter_interval) / 2, 0), radius=ion.R, facecolor='none', edgecolor='b'))
    gca.add_patch(plt.Circle(((impact_parameter - impact_parameter_interval) / 2, 0), radius=ion.R, facecolor='none', edgecolor='r'))

    # Turn off tick labels
    # ax.set_yticklabels([])
    # ax.set_xticklabels([])

def create_magnetic_field_graph(magnetic_field_x_event, magnetic_field_y_event, magnetic_field_y_event_nomodule):
    global gd
    # row 1, column 0
    plt.subplot(gd[1, 0])
    plt.title("Magnetic Field (B)")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.B Field event")

    plt.plot(impact_parameter_list, magnetic_field_x_event, 'bo-', label='|B(x)|')
    plt.plot(impact_parameter_list, magnetic_field_y_event, 'rs-', label='|B(y)|')
    plt.plot(impact_parameter_list, magnetic_field_y_event_nomodule, 'k.-', label='B(y)')

    plt.legend(loc='upper right', borderaxespad=0.1)

def create_electric_field_graph(electric_field_x_event, electric_field_y_event):
    global gd
    # row 1, column 1
    plt.subplot(gd[1, 1])
    plt.title("Electric Field (E)")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.E Field event")

    plt.plot(impact_parameter_list, electric_field_x_event, 'bo-', label='|E(x)|')
    plt.plot(impact_parameter_list, electric_field_y_event, 'r.-', label='|E(y)|')
    plt.legend(loc='upper right', borderaxespad=0.1)

def create_standard_deviation_graph(bx_module_e, by_module_e, by_nomodule_e, ex_module_e, ey_module_e):
    # 3 x 2 grid
    grid = gridspec.GridSpec(3, 2, wspace=0.4, hspace=1.0)

    plt.figure(num='HICS - Standard Deviation')
    # row 0, column 0
    plt.subplot(grid[0, 0])
    plt.title("Standard Deviation of |B(x)|")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.B Field event")
    plt.plot(impact_parameter_list, eBx_event, 'c.-', label='e.B Field |B(x)|')
    plt.errorbar(impact_parameter_list, eBx_event, bx_module_e, ecolor='g', linestyle='None', label='Error')
    plt.legend(loc='upper right', borderaxespad=0.1)

    # row 1, column 0
    plt.subplot(grid[1, 0])
    plt.title("Standard Deviation of |B(y)|")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.B Field event")
    plt.plot(impact_parameter_list, eBy_event, 'c.-', label='e.B Field |B(y)|')
    plt.errorbar(impact_parameter_list, eBy_event, by_module_e, ecolor='g', linestyle='None', label='Error')
    plt.legend(loc='upper right', borderaxespad=0.1)

    # row 2, column 0
    plt.subplot(grid[2, 0])
    plt.title("Standard Deviation of B(y)")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.B Field event")
    plt.plot(impact_parameter_list, eBy_event_nomodule, 'c.-', label='e.B Field B(y)')
    plt.errorbar(impact_parameter_list, eBy_event_nomodule, by_nomodule_e, ecolor='g', linestyle='None', label='Error')
    plt.legend(loc='upper right', borderaxespad=0.1)

    # row 0, column 1
    plt.subplot(grid[0, 1])
    plt.title("Standard Deviation of |E(x)|")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.E Field event")
    plt.plot(impact_parameter_list, eEx_event, 'k.-', label='e.E Field |E(x)|')
    plt.errorbar(impact_parameter_list, eEx_event, ex_module_e, ecolor='g', linestyle='None', label='Error')
    plt.legend(loc='upper right', borderaxespad=0.1)

    # row 1, column 1
    plt.subplot(grid[1, 1])
    plt.title("Standard Deviation of |E(y)|")
    plt.xlabel("$b (fm)$")
    plt.ylabel("e.E Field event")
    plt.plot(impact_parameter_list, eEy_event, 'k.-', label='e.E Field |E(y)|')
    plt.errorbar(impact_parameter_list, eEy_event, ey_module_e, ecolor='g', linestyle='None', label='Error')
    plt.legend(loc='upper right', borderaxespad=0.1)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Total execution time (seconds): " + str(time.time() - start_time))
    # show graphs
    plt.show()
