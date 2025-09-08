n = int(input())
A, B = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    A += a
    B += b
    print(A - B)