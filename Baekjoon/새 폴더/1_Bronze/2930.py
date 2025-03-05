r = int(input())
sanggeun = input()
n = int(input())
friends = [input() for _ in range(n)]
# 진행 라운드 수와 친구들과 상근이가 낼 수를 받아줍니다
points = 0
result = 0
# 낸 결과로 받을 점수와 미리 알았을경우 얻을 최대 점수를 담을 변수를 설정해줍니다
for i in range(r):
    RSP = [0, 0, 0]
    for j in range(n):
        if sanggeun[i] == 'R':
            if friends[j][i] == 'R':
                points += 1
                RSP[0] += 1
            elif friends[j][i] == 'S':
                points += 2
                RSP[1] += 1
            else:
                RSP[2] += 1
        elif sanggeun[i] == 'S':
            if friends[j][i] == 'S':
                points += 1
                RSP[1] += 1
            elif friends[j][i] == 'P':
                points += 2
                RSP[2] += 1
            else:
                RSP[0] += 1
        else:
            if friends[j][i] == 'P':
                points += 1
                RSP[2] += 1
            elif friends[j][i] == 'R':
                points += 2
                RSP[0] += 1
            else:
                RSP[1] += 1
    result += max([RSP[0] + RSP[1] * 2, RSP[1] + RSP[2] * 2, RSP[2] + RSP[0] * 2])
# 친구들이 낸 결과를 확인하며 얻은 점수와 미리 알았을경우 얻을 수 있는 최대 점수를 구해줍니다
print(points)
print(result)
# 결과를 출력해줍니다