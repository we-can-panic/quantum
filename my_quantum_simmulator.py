# 何やってるかわかるように基本これに全部書いていきます
import numpy as np
import random
from collections import Counter

class C:
  def __init__(self, n=1):
    self.qubits = [np.array([1, 0])]*n

  def x(self, *n):
    arr = np.array([[0, 1], [1, 0]])
    for i in n:
      self.qubits[i] = np.dot(self.qubits[i], arr)
    return self

  def y(self, *n):
    arr = np.array([[0, -1j], [1j, 0]])
    for i in n:
      self.qubits[i] = np.dot(self.qubits[i], arr)
    # print(self.qubits)
    return self

  def z(self, *n):
    arr = np.array([[1, 0], [0, -1]])
    for i in n:
      self.qubits[i] = np.dot(self.qubits[i], arr)
    # print(self.qubits)
    return self

  def h(self, *n):
    arr = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])
    for i in n:
      self.qubits[i] = np.dot(self.qubits[i], arr)
    # print(self.qubits)
    return self

  def cz(self, c, z):
    arr = np.array([[1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,-1]])
    c0, c1 = self.qubits[c]**2
    z0, z1 = self.qubits[z]**2
    print(c0,c1,z0,z1)
    src = np.array([c0*z0, c0*z1, c1*z0, c1*z1])
    dst = np.dot(src, arr) # absをかけるとzの意味がなく、かけないとコントロールビットが1にならない
    c0, c1 = dst[0]+dst[1], dst[2]+dst[3]
    z0, z1 = dst[0]+dst[2], dst[1]+dst[3]
    print(c0,c1,z0,z1)
    self.qubits[c] = np.sqrt(np.array([c0, c1]))
    self.qubits[z] = np.sqrt(np.array([z0, z1]))
    return self


  def m(self):
    self.qubits_real = [(np.abs(i)*100).astype(np.uint8) for i in self.qubits]
    return self

  def run(self, shots):
    # それぞれの状態に合わせて0と1の確率を用意
    qubits_prob = []
    self.m()
    for j in self.qubits_real:
      qubits_prob.append([0]*(j[0]**2*shots)+[1]*(j[1]**2*shots))
    print(len(qubits_prob[0]))#, len(qubits_prob[1]))
    # ↑のリストからランダムで値を抜き出す。これをshotsぶん繰り返す
    ret_list = []
    for i in range(shots):
      ret_str = ""
      for j in qubits_prob:
        ret_str += str(random.sample(j, 1)[0])
      ret_list.append(ret_str)
    return Counter(ret_list)


def test_cz():
  c = C(2).x(0).h(1).cz(0, 1)
  print("qbit", c.qubits)
  #print("q_real", c.qubits_real)
  print("res", c.run(100))

if __name__ == '__main__':
  test_cz()
  quit()
  print(C(2).x(0).run(100))
  print(C(2).y(0).run(100))
  print(C(2).z(0).run(100))
  print(C(2).h(0).run(100))
  print(C(1).h(0).z(0).h(0).run(100))
