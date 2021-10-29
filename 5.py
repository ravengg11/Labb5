from math import sqrt, pi
id = int(input("Номер элемента"))
if id == 1:
   R = float(input("радиус = "))
elif id == 2:
   R = float(input("радиус = ")) / 2
elif id == 3:
   R = float(input("радиус = ")) / 2 / pi
else:
   R = sqrt(float(input("радиус = ")) / pi)
D = 2 * R
L = 2 * pi * R
S = pi * R**2
if id == 1:
   print(D, L, S)
elif id == 2:
   print(R, L, S)
elif id == 3:
   print(R, D, S)
else:
   print(R, D, L)

