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

aceleradores:
    LHC
    RHIC
    SPS
    param -> 0 a 2*R

| Ion | Atom mass | Atom number | Energy (√sNN) | Collider |
| --- | --------- | ----------- | ------------- | -------- |
| Pb  | 206       | 82          | 2.76 TeV      | LHC      |
| Au  | 197       | 79          | 200  GeV      | RHIC     |
| 1   | 1         | 0           |               |          |