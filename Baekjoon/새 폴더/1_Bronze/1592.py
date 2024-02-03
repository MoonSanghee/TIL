n, m, l = map(int, input().split())
# 세 수를 받아줍니다.
people = [0] * n
# 사람을 리스트로 받아줍니다.
cnt = 0
# 볼이 몇 번 뜅겼는지 담아줄 변수를 정해줍니다.
ball = 0
# 볼의 위치를 담을 변수를 정해줍니다.
while people[ball] < m - 1:
    # 볼을 받은 횟수가 m보다 작다면 볼을 다시 튕겨줍니다.
    people[ball] += 1
    cnt += 1
    # 볼을 받은 사람과 횟수를 표시해줍니다.
    if people[ball] % 2:
        ball += l
        ball %= n
        # 볼을 홀수번째 받았다면 시계방향
    else:
        ball -= l
        ball %= n
        # 짝수번째 받은것이라면 반시계방향으로 볼을 튕겨줍니다.
print(cnt)
# 볼을 몇 번 튕겼는지 출력해줍니다.