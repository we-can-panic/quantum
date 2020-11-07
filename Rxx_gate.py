import numpy as np

def Rxx_gate():
  theta = 1.5*np.pi

  sin = -1j*np.sin(theta)
  cos = np.cos(theta)

  rxx = np.array([
  [cos,0,0,sin],
  [0,cos,sin,0],
  [0,sin,cos,0],
  [sin,0,0,cos]
  ])

  indexes = "00,01,10,11".split(",")

  qubits_prob = np.array([0,0,0,1])

  after_qubits_prob = np.dot(qubits_prob, rxx)

  for i, q, aq in zip(indexes, qubits_prob, after_qubits_prob):
    print(i, q, "->", np.abs(aq).round(2))

if __name__ == '__main__':
  Rxx_gate()
