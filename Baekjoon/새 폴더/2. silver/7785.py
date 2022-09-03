log_cnt = int(input())
name = dict()

for i in range(log_cnt):
    a, b = map(str, input().split())
    if b == 'enter':
        name[a] = 1
    else:
        del name[a]

name1 = sorted(name.keys(), reverse=True)

for i in name1:
    print(i)