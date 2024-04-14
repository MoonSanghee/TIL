result = 0
# 결과를 담을 변수를 설정해줍니다.
while True:
    number = int(input())
    if number == -1:
        break
    result += number
# -1이 나올때까지 수를 받아 최종 결과에 더해줍니다.
print(result)
# 배팅한 최종 금액을 출력해줍니다.