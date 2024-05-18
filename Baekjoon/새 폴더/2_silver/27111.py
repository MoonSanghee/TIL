n = int(input())
check = [0] * 200001
cnt = 0
# 주어지는 출입 기록의 수와 출입 결과를 담을 리스트 누적을 담을 변수를 설정해줍니다.
for _ in range(n):
    a, b = map(int, input().split())
    if check[a] == b:
        cnt += 1
    # a의 행위가 기록된 행위와 같다면 누락된 기록이 있어야하므로 1을 추가해줍니다.
    check[a] = b
    # a의 b 행위를 표시해줍니다

print(cnt + check.count(1))
# 나간 기록이 없는 사람도 기록이 누락된 기록이 있는것이므로 확인하여 더한 값을 출력해줍니다.