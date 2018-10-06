# HICS
Heavy Ion Collider Simulator

##Requirements:

HICS requires [Python](https://www.python.org/) 3.7.x^ to run.

After install python install the follow libraries, know as SciPy:
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

| Ion | Atom mass | Atom number | Used by |
| --- | --------- | ----------- | ------- |
| 0   | 1         | 1           | 4       |
| 1   | 0         | 1           | 3       |
| 1   | 1         | 0           | 2       |