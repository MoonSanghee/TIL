n = int(input())
# 참가하는 팀의 수를 받아줍니다
points = [0] * (n + 1)
# 점수를 담을 변수를 설정해줍니다
for _ in range(n * (n - 1) // 2):
    A, B, C, D = map(int, input().split())
    if C == D:
        points[A] += 1
        points[B] += 1
    elif C > D:
        points[A] += 3
    else:
        points[B] += 3
    # 경기 결과를 받고 경기 결과에 따라 승점을 추가해줍니다

for i in range(n):
    rank = 1
    for j in range(n):
        if points[i + 1] < points[j + 1]:
            rank += 1
    print(rank)
    # 각 팀을 순회하며 순위를 확인해 출력해줍니다