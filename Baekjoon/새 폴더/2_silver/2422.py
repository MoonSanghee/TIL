n, m = int(input())
# 아이스크림의 종류와 섞으면 안 되는 조합의 수를 받아줍니다.
ban = [[False for _ in range(n)] for _ in range(n)]
# 섞으면 안 되는 조합을 표시할 이중리스트를 만들어줍니다.
for _ in range(m):
    a, b = map(int, input().split())
    ban[a - 1][b - 1] = True
    ban[b - 1][a - 1] = True
    # 섞으면 안 되는 조합을 받아 표시해줍니다.

result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not ban[i][j] and not ban[j][k] and not ban[k][i]:
                result += 1
# 아이스크림을 순회하며 3가지 아이스크림을 뽑아서 섞으면 안 되는 조합이 있는지 확인하고 없다면 
# 만들수 있는 조합의 결과를 갱신해줍니다.
print(result)
# 결과를 출력해줍니다.