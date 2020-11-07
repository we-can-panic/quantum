import numpy as np

ket0 = np.array([1, 0]).reshape(2,1)
bra0 = ket0.reshape(1, 2)
ket1 = np.array([0, 1]).reshape(2,1)
bra1 = ket1.reshape(1, 2)

X = np.array([[0,1], [1, 0]])

print(np.dot(bra0, ket0))
print(np.dot(bra1, ket1))
print(np.dot(ket0, bra0))
print(np.dot(ket1, bra1))
