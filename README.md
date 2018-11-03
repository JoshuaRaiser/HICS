# HICS
Heavy Ion Collider Simulator

##Requirements:

HICS requires [Python](https://www.python.org/) 3.7.x^ to run.

After install python, first install the follow libraries, know as [SciPy](https://www.scipy.org/).

By command line:
```sh
$ python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

## Ion's type
Already implemented:

| Ion | Atom mass | Atom number | Energy at collision (√sNN) | Collider |
| --- | --------- | ----------- | -------------------------- | -------- |
| Pb  | 206       | 82          | 2.76 TeV                   | LHC      |
| Au  | 197       | 79          | 200  GeV                   | RHIC     |

Implemented for all ions:

* Magnetic Field
* Electric Field
* Standard Deviation

Also Monte Carlo implemented:

* Metropolis-hastings Algorithm (used to show the incidences in nuclear density calculate)


## Usage
To usage the HICS - Heavy Ion Collider Simulator, follow:

* Open and configure the variables in the [configurations file.py](configurations_hics.py)

This can do by any text editor. In this archive, above mentioned, read with attention the instructions and variables operations.


After configurate according to what is desired, save the file and run de algorithm at [structured_hics.py](structured_hics.py).

By command line:
```sh
$ python structured_hics.py
```

