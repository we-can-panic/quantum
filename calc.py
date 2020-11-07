# 古典コンピュータの論理演算は、NANDの組み合わせですべて可能である
# なので、量子コンピュータでNANDを作れれば、すべての論理演算が可能となる

from blueqat import Circuit as C

def nand(a, b):
  # circ[] = a, b, result
  circ = C(3)
  if a:
    circ.x[0]
  if b:
    circ.x[1]
  circ.ccx[0,1,2]
  return circ

def nand_test():
  for a in range(2):
    for b in range(2):
      print("{} * {} = {}".format(a, b, nand(a,b).m[:].run(100)))

# 量子状態の非破壊測定
def measure(v, w):
  # v, wの状態をresultにトレース
  # result = |<v|w>|^2
  # circ[] = v, w, result
  """
  <v|w>について
  ・vの複素共役＊w
  v : w =
  0 : 0 = (0, -1) * (0, 1)^T = -1
  0 : 1 = (0, -1) * (1, 0)^T = 0
  1 : 0 = (1, -0) * (0, 1)^T = 0
  1 : 1 = (1, -0) * (1, 0)^T = 1
  """
  circ = C(3)
  if v:
    circ.x[0]
  if w:
    circ.x[1]
  circ.h[2]
  circ.ccz[0,1,2]
  circ.h[2]
  return circ

def measure_test():
  for a in range(2):
    for b in range(2):
      print("{} * {} = {}".format(a, b, nand(a,b).m[:].run(100)))

def Grover_11():
  # c = 00 or 01 or 10 or 11
  c = C(2).h[:]
  c.cz[1, 0]
  # c.h[0].cx[1,0].h[0]
  c.h[:]
  c.x[0].x[1]
  c.cz[1, 0]
  # c.h[0].cx[1,0].h[0]
  c.x[:]
  c.h[:]
  return c

if __name__ == '__main__':
  # measure_test()
  print(Grover_11().m[:].run(100))
