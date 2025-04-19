n = int(input())
maps = [input() for _ in range(n)]
# 마방진의 크기와 마방진을 받아줍니다
flag = True
for i in range(n):
    for j in range(n):
        if maps[i][j] != maps[j][i]:
            flag = False
# 마방진을 순회하며 사토르 마방진인지 확인해줍니다
if flag:
    print("YES")
else:
    print("NO")
# 결과를 출력해줍니다