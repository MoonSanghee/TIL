a, b, c = map(int, input().split())
s, v = map(int, input().split())
l = int(input()) * 100
# 주어지는 변수들을 받고 현재 레벨 * 100을 경험치로 설정해줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
while l < 25000:
    # 250레벨을 달성할때까지 반복합니다
    if v:
        v -= 1
        for i in range(30):
            l += c
            result += 1
            if l >= 25000:
                break
        # v값이 있다면 30분동안 매분 c의 경험치를 받고 목표를 달성했는지 확인합니다
    elif s:
        s -= 1
        for i in range(30):
            l += b
            result += 1
            if l >= 25000:
                break
        # v가 없고 s만 있다면 매분 b의 경험치를 받고 목표를 달성했는지 확인합니다
    else:
        result += 1
        l += a
        # v와 s가 남지 않았다면 매분 a의 경험치를 받으며 목표를 달성했는지 확인해줍니다

print(result)
# 소요되는 시간을 출력해줍니다