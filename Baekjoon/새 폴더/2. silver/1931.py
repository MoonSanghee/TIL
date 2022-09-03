n = int(input())
numbers = []
for i in range(n):
    s, e = map(int, input().split())
    numbers.append([s, e])

numbers.sort(key = lambda x: (x[1], x[0]))
# 람다함수를 이용하여 마치는시간, 시작시간 순으로 정렬해주는게 핵심이다.
print(numbers)
cnt = 1
end = numbers[0][1]
for i in range(1, n):
    if numbers[i][0] >= end:
        cnt += 1
        end = numbers[i][1]
print(cnt)