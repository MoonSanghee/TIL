n = int(input())
weather = list(map(int, input().split()))
# 확일할 날의 수와 예보를 받아줍니다
result = 0
now = 0
# 날씨에 따라 변한 분노와 누적 분노를 담을 변수를 설정해줍니다
for i in range(n):
    if weather[i] == 0:now -=1
    else:now += 1
    result += now
# 비가 오는지 확인하고 기분을 갱신한뒤 누적값에 더해줍니다
print(result)
# 결과를 출력해줍니다