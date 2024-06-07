n, m = map(int, input().split())
points = list(map(int, input().split()))
# 문제 수와 응시생의 수를 받고 배점을 받아줍니다.
highest = 0
number = 100001
# 최고점을 담을 변수와 최고점을 받은 학생을 담을 변수를 설정해줍니다.
# 학생의 번호는 100000까지이므로 무조건 값이 갱신되도록 학생의 번호 범위 밖의 수를 최초에 설정해줍니다.
for i in range(m):
    answer = list(input().split())
    # 제출한 답지를 받아줍니다.
    get = 0
    for j in range(n):
        if answer[j + 1] == "O":
            get += points[j]
    # 맞은 문제를 확인하여 득점을 담아줍니다.
    if get > highest:
        highest = get
        number = int(answer[0])
    elif get == highest:
        number = min(number, int(answer[0]))
    # 최고점을 갱신하였다면 최고득점자를 갱신해주고 최고점과 동률이라면 낮은 번호로 갱신해줍니다.
print(number, highest)
# 최고 득점자와 점수를 출력해줍니다.