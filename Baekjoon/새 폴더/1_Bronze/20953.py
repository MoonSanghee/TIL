import sys
input = sys.stdin.readline

def dolmen(a, b):
    n = a + b
    return (n * n * (n - 1)) // 2

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(dolmen(a, b))