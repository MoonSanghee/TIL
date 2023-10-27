t = int(input())
# 테스트 케이스의 개수를 받아줍니다.
for _ in range(t):
    score = sorted(list(map(int, input().split())))
    # 점수를 받아 오름차순으로 정렬해줍니다.
    point = sum(score[1:4])
    # 최고점과 최저점을 제외한 3점수의 합을 구해줍니다.
    if score[3] - score[1] >= 4:
        print('KIN')
        # 두 번째로 높은 득점과 두 번째로 낮은 득점의 차이가 4이상이라면 KIN을 출력해줍니다.
    else:
        print(point)
        # 아니라면 최고점과 최저점을 제외한 점수 합을 출력해줍니다.