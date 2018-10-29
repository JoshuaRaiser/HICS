import math
import random
import matplotlib.pyplot as plt
from collections import OrderedDict
from scipy.optimize import fsolve
from objects.ion import Ion

ion = Ion()

F = 0
step = 0.5
cases = 1000000

def main():
    global F
    count = {}

    ion.define_gold_ion()
    for index in range(cases):
        F = random.uniform(0, 1)
        r = fsolve(__calculate_find_root_integrated, 0.0)[0]

        r_int = int(r)
        r_decimals = round(r - r_int, 2)

        k = str(r_int) if r_decimals < step else str(r_int + step)

        count[k] = count[k] + 1 if k in count.keys() else 1

    print(count)
    print('sorted keys: ' + str(sorted(count)))
    count_plot(count)

def count_plot(count):
    plt.figure(num='HICS - Metropolis Hastings for Nuclear Density')
    plt.title("Incidence's cases of Nuclear Density")
    plt.xlabel("step (interval of " + str(step) + ")")
    plt.ylabel("incidence in " + str(cases) + " cases")

    ordered_by_key = OrderedDict(sorted(count.items(), key=lambda x: float(x[0])))

    plt.bar(range(len(count)), ordered_by_key.values(), color='black', edgecolor='black', align='center')
    plt.xticks(range(len(count)), ordered_by_key.keys())

    plt.show()

def __calculate_find_root_integrated(x):
    p0 = (1 / (ion.a * math.log(math.exp(ion.R / ion.a) + 1)))
    next_x = p0 * (x - ion.a * math.log((1 + math.exp((x - ion.R) / ion.a) / (1 + math.exp(-ion.R / ion.a))))) - F
    #next_x = 1.0/ion.R * (x - ion.a * math.log(math.exp(ion.R/ion.a) + math.exp(x/ion.a)) + ion.R) - F
    return next_x

if __name__ == "__main__":
    main()
