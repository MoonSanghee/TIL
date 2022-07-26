import sys

sys.stdin = open("1946_input.txt", "r")

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    c = ''    
    for j in range(n):
        a, b = input().split()
        c += a*int(b)
    print(f'#{i}')
    for k in range((len(c)//10) + 1):
        print(c[10*(k):10*(k + 1)])