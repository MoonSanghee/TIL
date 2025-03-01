base = set()
for i in 'roygbiv':
    base.add(i)

Small = set()
Capital = set()
flag = False
flag2 = False

n = int(input())
for i in input():
    if i.isupper():
        Capital.add(i.lower())
    else:
        Small.add(i)

for i in base:
    if i not in Capital:
        break
else:
    flag = True

for i in base:
    if i not in Small:
        break
else:
    flag2 = True

if flag and flag2:
    print('YeS')
elif flag:
    print("YES")
elif flag2:
    print("yes")
else:
    print("NO!")