n, k = map(int, input().split())
days = list(map(int, input().split()))
# 전체 일수와 확인할 연속한 일수를 받고 날짜별 온도를 받아줍니다.
result = sum(days[i] for i in range(k))
check = result
# 첫 k일동안 온도를 더해 연속한 일수의 온도를 담을 변수를 만들어줍니다.
for i in range(k, n):
    check += days[i]
    check -= days[i - k]
    result = max(result, check)
# 이후 n일 안에서 연속한 k일 동안의 연속한 날의 온도 합이 가장 큰 값을 구해줍니다.
print(result)
# 결과를 출력해줍니다.