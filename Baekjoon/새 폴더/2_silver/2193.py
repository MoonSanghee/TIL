# 나의 풀이
numbers = [(0, 1), (1, 0)]
n = int(input())
for i in range(2, n):
    zero, one = numbers[i - 1]
    a = zero + one
    b = zero
    numbers.append((a, b))
print(sum(numbers[n - 1]))

