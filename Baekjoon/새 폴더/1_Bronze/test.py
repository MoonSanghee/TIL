import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
least = max(math.ceil(b / d), math.ceil(a / c))
print(l - least)