numbers = []
num_cnt = dict()
for i in range(10):
    num = int(input())
    numbers.append(num)
    if num in num_cnt:
        num_cnt[num] += 1
    else:
        num_cnt[num] = 1

avg = sum(numbers) // 10
most = 0
cnt = 0
for i in numbers:
    value = num_cnt[i]
    if value > cnt:
        most = i
        cnt = value

print(avg)
print(most)