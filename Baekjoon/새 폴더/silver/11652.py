n = int(input())
numbers = dict()

for i in range(n):
    num = int(input())
    if num not in numbers:
        numbers[num] = 1
    else:
        numbers[num] += 1

count = 0
for i in numbers:
    if numbers[i] > count:
        most_nums = []
        most_nums.append(i)
        count = numbers[i]
    elif numbers[i] == count:
        most_nums.append(i)

print(min(most_nums))