import sys

sys.stdin = open("1976_input.txt", "r")

t = int(input())
for i in range(t):
    a, b, c, d = map(int, input().split())
    h = a + c
    m = b + d    
    if b + d >= 60:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
    print(f'#{i + 1} {h} {m}')
