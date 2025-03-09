n = int(input()) + 1
n = bin(n)[3:]

n = n.replace('0', '4')
n = n.replace('1', '7')
print(n)