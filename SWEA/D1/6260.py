code = input()
big = 0
small = 0

for i in code:
    if i.isupper():
        big += 1
    elif i.islower():
        small += 1

print(f'UPPER CASE {big}')
print(f'LOWER CASE {small}')