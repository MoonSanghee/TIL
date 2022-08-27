t = int(input())

from audioop import reverse


under_10000 = []
for i in range(2, 10001):
    check_list = []
    for j in range(1, i + 1):
        if i % j == 0:
            check_list.append(j)
    if len(check_list) == 2:
        under_10000.append(max(check_list))
reverse_10000 = under_10000[::-1]
# print(len(under_10000))
for i in range(t):
    n = int(input())
    for j in under_10000:
        for k in under_10000:
            if (under_10000[j] + under_10000[k]) == n:
                print(f'{j} {k}')
                break



