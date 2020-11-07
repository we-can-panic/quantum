import math as M

def cos(deg):
  return round(M.cos(M.radians(deg)), 2)

def sin(deg):
  return round(M.sin(M.radians(deg)), 2)

def tan(deg):
  return round(M.tan(M.radians(deg)), 2)

def acos(rat):
  return round(M.degrees(M.acos(rat)), 2)

def asin(rat):
  return round(M.degrees(M.asin(rat)), 2)

def atan(rat):
  return round(M.degrees(M.atan(rat)), 2)
