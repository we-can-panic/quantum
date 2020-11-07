from blueqat import Circuit as C
from blueqat import vqe
from blueqat.pauli import qubo_bit as q

# SWAP(2量子ビットの値を入れ替えるゲート)
# -> 01と10の確率を入れ替えるゲート
"""
      [brank]     cx[0,1]     cx[1,0]     cx[0,1]
[00]  1 0 0 0     1 0 0 0     1 0 0 0     1 0 0 0
[01]  0 1 0 0  >  0 1 0 0  >  0 0 1 0  >  0 0 1 0
[10]  0 0 1 0     0 0 0 1     0 0 0 1     0 1 0 0
[11]  0 0 0 1     0 0 1 0     0 1 0 0     0 0 0 1
"""
a = C(2)
a.x[0]
a.cx[1,0]
a.cx[0,1]
a.cx[1,0]
a = a.m[:].run(100)

print(a)
