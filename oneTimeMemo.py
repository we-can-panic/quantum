import numpy as np
from my_quantum_simmulator import C

c = C(1).h(0).z(0)

print(c.qubits)


print(c.run(100))
