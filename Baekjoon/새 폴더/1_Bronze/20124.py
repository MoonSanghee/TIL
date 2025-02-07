n = int(input())

score = 0
names = []

for _ in range(n):
    name, point = input().split()
    if int(point) > score:
        score = int(point)
        names = [name]
    elif int(point) == score:
        names.append(name)

names.sort()

print(names[0])