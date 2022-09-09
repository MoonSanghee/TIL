n = str(input())
num = []
check = ['1', '2', '3', '4', '5', '7', '8', '0', '6']
for i in check:
    if i == '6':
        if (n.count('6') + n.count('9')) % 2 == 0:
            num.append((n.count('6') + n.count('9')) // 2)
        else:
            num.append(((n.count('6') + n.count('9')) // 2) + 1)
    else:
        num.append(n.count(i))
print(max(num))