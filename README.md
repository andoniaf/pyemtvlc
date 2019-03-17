# pyemtvlc  
[![PyPI version](https://badge.fury.io/py/pyemtvlc.svg)](https://badge.fury.io/py/pyemtvlc) [![Build Status](https://travis-ci.org/andoniaf/pyemtvlc.svg?branch=master)](https://travis-ci.org/andoniaf/pyemtvlc)

Python package to query EMT Valencia (bus).

![](https://raw.githubusercontent.com/andoniaf/pyemtvlc/master/img/pyemtvlc_logo_small.png)

Information obtained from [EMT Valencia](http://movil.emtvalencia.es).

# Examples

- Info about all lines of the bus stop. (636):
```
➜ pyemtvlc 636  
Parada: 636
7: Pl. Espanya - 7 min.
13: Pta.de la Mar - 8 min.
7: Pl. Espanya - 25 min.
13: Pta.de la Mar - 44 min.
N7: Pl. Ajuntament - 22:38
N7: Pl. Ajuntament - 23:03
```

- Info about one line (7) of the bus stop (636):
```
 ➜ pyemtvlc 636 7
Parada: 636
7: Pl. Espanya - 22 min.
7: Pl. Espanya - 46 min.
```

------
