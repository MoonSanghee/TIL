n,m = map(int, input().split())

people = dict()
for i in range(n):
    name = input()
    if name not in people:
        people[name] = 1

for i in range(m):
    name = input()
    if name not in people:
        people[name] = 1
    else:
        people[name] += 1

both = []
for i in people:
    if people[i] == 2:
        both.append(i)

both = sorted(both)
print(len(both))
for i in both:
    print(i)