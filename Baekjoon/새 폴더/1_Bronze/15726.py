a, b, c = map(int, input().split())
A = a * b/ c
B = a / b * c
print(int(max(A, B)))