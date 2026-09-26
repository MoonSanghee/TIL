students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
d = dict()

for i in students:
    d[i] = d.get(i, 0) + 1

print(d)