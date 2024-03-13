import sys
input = sys.stdin.readline

t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for _ in range(t):
    n = int(input())
    people = list(map(str, input().split()))
    # 사람의 수와 성향을 받아줍니다.
    total = 1000000
    # 최종 결과를 담을 변수를 설정해줍니다
    if n > 32:
        print(0)
        # 16가지 유형의 성향이 있는데 33명 이상일 경우 같은 성향이 3명이상 존재하므로 0을 출력해주어야합니다.
    else:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    result = 0
                    for x in range(4):
                        if people[i][x] != people[j][x]:
                            result += 1
                        if people[j][x] != people[k][x]:
                            result += 1
                        if people[k][x] != people[i][x]:
                            result += 1
                    # 3명의 사람을 선택하여 성향을 확인해 다른 성향이라면 변수에 담아줍니다.
                    total = min(result, total)
                    # 현재 선택한 3명의 성향 차이를 저장된 최솟값과 비교하여 갱신해줍니다.
        print(total)
        # 마음의 거리가 가장 가까운 값을 출력해줍니다.