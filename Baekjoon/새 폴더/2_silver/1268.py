n = int(input())
# 학생수를 받아줍니다.
infos = [list(map(int, input().split())) for _ in range(n)]
check = [[0 for _ in range(n)] for _ in range(n)]
# 학생들의 학년별 기록과 두 학생간의 같은반 여부를 확인할 리스트를 만들어줍니다.
for i in range(n):
    for j in range(i + 1, n):
        for k in range(5):
            if infos[i][k] == infos[j][k]:
                check[i][j] = 1
                check[j][i] = 1
# 모든 학생들을 비교하여 같은반이었으면 표시하여줍니다
result = []
for data in check:
    result.append(sum(data))
# 각 학생들이 받을수 있는 득점의 합을 차례로 리스트에 담아줍니다.
print(result.index(max(result)) + 1)
# 인덱스값은 0부터 시작하므로 index메서드를 이용해 찾은 사람에 1을 더한값을 출력해줍니다.