from math import pi

T = [2 * pi * int(i) for i in input().split(',')]
for j in T[:-1]:
    print("%0.2f"%j, end=', ')
print("%0.2f"%T[-1])