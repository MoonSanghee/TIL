# SWEA 6190
t = int(input())
for test in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    result = 1
    for i in range(n):
        for j in range(i + 1, n):
            num = numbers[i] * numbers[j]
            if num < result:
                break
            if list(map(int, str(num))) == sorted(list(map(int, str(num)))):
                result = num
    print(result)