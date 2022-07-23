# 8-2 문제번호 2581

m = int(input())
n = int(input())
col = []
for i in range(m, n + 1):
    check_list = []
    for j in range(1, i + 1):
        if i % j == 0:
            check_list.append(j)
    if len(check_list) == 2:
        col.append(max(check_list))
if len(col) == 0:
    print(-1)
else:
    print(sum(col))
    print(min(col))