n = int(input())
commands = input()
# 주어지는 입력의 길이와 입력을 받아줍니다
S, L = 0, 0
cnt = 0
# 사전기술 S와L이 나온 횟수를 담을 변수와 전체 기술 사용 횟수를 담을 변수를 설정해줍니다
for i in commands:
    if i == "S":
        S += 1
    elif i == "L":
        L += 1
        # S나 L이라면 사전 기술 횟수를 갱신해줍니다
    elif i == "K":
        if S > 0:
            S -= 1
            cnt += 1
        else:
            break
    elif i == "R":
        if L > 0:
            L -= 1
            cnt += 1
        else:
            break
        # K나 R이라면 사전기술이 충분하다면 값을 갱신하고 아니면 멈추어줍니다
    else:
        cnt += 1
        # 개별 기술이라면 결과값을 갱신해줍니다

print(cnt)
# 결과를 출력해줍니다