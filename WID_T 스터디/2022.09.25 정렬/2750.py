

# 버블정렬
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
for i in range(n):
    for j in range(n - i - 1):
        if li[j + 1] < li[j]:
            li[j + 1], li[j] = li[j], li[j + 1]
for i in li:
    print(i)