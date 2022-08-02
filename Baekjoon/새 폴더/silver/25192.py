import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
name_set = []

for i in range(n):
    name = input().strip()
    if name == 'ENTER':
        cnt += len(set(name_set))
        name_set = []
    else:
        name_set.append(name)

cnt += len(set(name_set))

print(cnt)