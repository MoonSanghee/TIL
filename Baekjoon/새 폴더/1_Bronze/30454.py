n, l = map(int, input().split())
# 얼룩말의 마리수와 길이를 받아줍니다
result = 0
line = 0
# 줄무늬의 수와 개체수를 담을 변수를 설정해줍니다
for _ in range(n):
    zebra = input()
    black = 0
    # 얼룩말을 입력받고 검은 줄의 수를 담을 변수를 설정해줍니다
    if zebra[0] == '1':
        black += 1
    # 첫 무늬가 검은색이라면 검정줄이 한 줄 더 있다고 표시해줍니다
    for i in range(1, l):
        if zebra[i - 1] == '0' and zebra[i] == '1':
            black += 1
    # 직전 색이 흰색이고 현재 색이 검은색이라면 줄이 추가되었다고 표시해줍니다
    if black > line:
        line = black
        result = 1
    # 검은 줄의 수가 갱신되었다면 검은 줄의 최대값을 갱신하고 개체수를 1로 만들어줍니다
    elif black == line:
        result += 1
    # 검은 줄의 최대수가 동일하다면 개체수를 증가시켜줍니다

print(line, result)
# 최대 줄의 수와 개체수를 출력해줍니다