# HICS
Heavy Ion Collider Simulator

##Requirements:

HICS requires [Python](https://www.python.org/) 3.7.x^ to run.

After install python install the follow libraries by command line, know as [SciPy](https://www.scipy.org/):
```sh
$ python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

## Ion's type
Already implemented:

| Ion | Atom mass | Atom number | Energy (√sNN) | Collider |
| --- | --------- | ----------- | ------------- | -------- |
| Pb  | 206       | 82          | 2.76 TeV      | LHC      |
| Au  | 197       | 79          | 200  GeV      | RHIC     |

Implemented for all ions:

* Magnetic Field
* Electric Field
* Standard Deviation

Also Monte Carlo implemented:

* Metropolis-hastings Algorithm (used to show the incidences in nuclear density calculate)


## Usage
To usage the developed programa, follow:

* Open and configure the variables in the [configurations file](configurations_hics.py)

After configurations, save the file and run de algorithm at [structured_hics](structured_hics.py).