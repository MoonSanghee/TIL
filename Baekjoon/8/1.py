# 8-1 문제번호 1978

n = int(input())
cnt = 0
a = list(map(int, input().split()))

for i in range(n):
    b = []
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            b.append(j)
    if len(b) == 2:
        cnt += 1
# for i in range(n):
#     a = int(input())
#     b = []
#     for j in range(1, a + 1) :
#         if a % j == 0:
#             b.append(j)
#     if len(b) == 2:
#         cnt += 1
# print(cnt)

