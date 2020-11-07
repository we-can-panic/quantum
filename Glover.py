from my_quantum_simmulator import C as C1
from blueqat import Circuit as C2

def glover_11():
  r1 = C1(1).h(0).z(0).h(0).x(0).z(0).x(0).h(0).run(100)
  r2 = C2(1).h[0].z[0].h[0].x[0].z[0].x[0].h[0].m[0].run(100)
  r3 = C2(2).h[:].cz[1,0].h[:].x[:].cz[1,0].x[:].h[:].m[:].run(100)
  print(r1)
  print(r2)
  print(r3)

if __name__ == '__main__':
  glover_11()
