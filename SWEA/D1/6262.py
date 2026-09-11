code = input()
d = dict()

for i in code:
    d[i] = d.get(i, 0) + 1

for k in d:
    print(f'{k},{d[k]}')