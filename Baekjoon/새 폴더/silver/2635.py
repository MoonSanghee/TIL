n = int(input())
longest = []
for i in range(n + 1):
    numbers = [n, i]
    while True:
        if numbers[-2] < numbers[-1]:
            break
        numbers.append(numbers[-2] - numbers[-1])
    if len(numbers) > len(longest):
        longest = numbers
print(len(longest))
print(*longest)