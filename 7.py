import math
X = float(input("Первое число = "))
N = int(input("Второе число = "))
T = 1.0
S = 1.0
Fa = 1.0
for i in range(1,2*N):
    Fa = Fa*i
    S = S*X
    if i//2 == 0:
        S = S*(-1)
        T = T+S/Fa
print (T)