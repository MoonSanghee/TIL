n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다
odds = 0
evens = 0
sort_by_odd = 0
sort_by_even = 0
# 짝수와 홀수의 개수와 짝수를 옮길때와 홀수를 옮길때 이동이 얼마나 필요한지 담을 변수를 설정해줍니다
for i in range(n):
    if numbers[i] % 2:
        odds += 1
        sort_by_odd += evens
    else:
        sort_by_even += odds
        evens += 1
# 수열의 각 자리가 홀수인지 짝수인지를 확인하여 얼마나 이동을 시켜야하는지 값을 갱신해줍니다
print(min(sort_by_even, sort_by_odd))
# 둘 중 작은값을 출력해줍니다