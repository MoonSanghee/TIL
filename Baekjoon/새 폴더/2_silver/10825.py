import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    x = list(map(str, input().split()))
    li.append(x)

li.sort(key = lambda x :(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in li:
    print(i[0])