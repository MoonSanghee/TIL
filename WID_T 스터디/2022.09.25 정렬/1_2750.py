# 버블정렬
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in range(n - 1):
    check = numbers[:n - i]
    for j in range(len(check) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

for i in numbers:
    print(i)

n = int(input())

# # 삽입정렬 풀이
# n = int(input())
# li = []
# for i in range(n):
#     li.append(int(input()))

# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if li[j - 1] > li[j]:
#             li[j - 1], li[j] = li[j], li[j - 1]
#         else:
#             break

# for i in range(n):
#     print(li[i])