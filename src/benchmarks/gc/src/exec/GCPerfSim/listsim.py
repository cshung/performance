#%%

import pandas as pd
from random import *

Size = 100
D = {}
N = [1] * Size
L = Size
R = Size
p = 50

for i in range(0, Size + 1):
    D[i] = 0

for i in range(0, 1000000):
    toremove = randint(0, R - 1)
    N[toremove] = N[toremove] - 1
    if N[toremove] == 0:
        N[toremove] = N[R - 1]
        N[R - 1] = 0
        R = R - 1
    tocreate = randint(0, 100)
    if tocreate < p: 
        N[R] = N[R] + 1
        R = R + 1
    else:
        if R == 1:
            toappend = 0
        else:
            toappend = randint(0, R - 1)
        N[toappend] = N[toappend] + 1
    for n in N:
        D[n] = D[n] + 1
print(D)

keys = []
counts = []
for i in range(1, Size + 1):
    keys.append(i)
    counts.append(D[i])
dict = {}
dict["keys"] = keys
dict["counts"] = counts
df = pd.DataFrame(dict)
df.plot()

# %%
print(1237228 / (1237228 + 499897 + 254326))
print(499897 / (1237228 + 499897 + 254326))
print(254326 / (1237228 + 499897 + 254326))
# %%
