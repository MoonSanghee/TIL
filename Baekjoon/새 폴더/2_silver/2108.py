n = int(input())
numbers = []
cnt = dict()
for i in range(n):
    num = int(input())
    numbers.append(num)
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
numbers.sort()
maxi = 1
result = []
for i in cnt:
    if maxi < cnt[i]:
        maxi = cnt[i]
        result = [i]
    elif maxi == cnt[i]:
        result.append(i)
result.sort()
print(round(sum(numbers)/n))
print(numbers[n//2])
if len(result) == 1:
    print(result[0])
else:
    print(result[1])
print(abs(numbers[-1] - numbers[0]))
# print(cnt)