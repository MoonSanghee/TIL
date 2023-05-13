import sys
input = sys.stdin.readline

k, l = map(int, input().split())

wait = dict()

for i in range(l):
    num = input().strip()
    wait[num] = i

result = sorted(wait.items(), key = lambda x:x[1])

if (k > len(result)):
    k = len(result)

for i in range(k):
    print(result[i][0])