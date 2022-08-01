a = int(input())
runners = dict()

for i in range(a):
    name = input().rstrip()
    if name in runners:
        runners[name] += 1
    else:
        runners[name] = 1

for i in range(a - 1):
    name = input().rstrip()
    runners[name] -= 1

for i in runners:
    if runners[i] == 1:
        print(i)
        break
