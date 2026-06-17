# pyemtvlc  
[![PyPI version](https://badge.fury.io/py/pyemtvlc.svg)](https://badge.fury.io/py/pyemtvlc)

Python package to query EMT Valencia (bus).

![](https://raw.githubusercontent.com/andoniaf/pyemtvlc/master/img/pyemtvlc_logo_small.png)

Information obtained from [EMT Valencia](https://geoportal.emtvalencia.es).

# Examples

- Info about all lines of the bus stop. (1054):
```
➜ pyemtvlc 1054
Parada: 1054
C2 Av. Arago - 7 min.
10 Benimaclet - 7 min.
10 Benimaclet - 16 min.
12 C.Art.Faller - 16 min.
93 Pass. Marítim - 18 min.
C2 Av. Arago - 20 min.
93 Pass. Marítim - 23 min.
12 C.Art.Faller - 29 min.
```

- Info about one line (12) of the bus stop (1054):
```
➜ pyemtvlc 1054 12
Parada: 1054
12 C.Art.Faller - 16 min.
12 C.Art.Faller - 29 min.
```

------
