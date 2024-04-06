from itertools import combinations

n, m = map(int, input().split())
point = [list(map(int, input().split())) for _ in range(n)]
# 사람의 수와 치킨 종류의 수, 회원별 선호도를 받아줍니다.
result = 0
# 결과값을 담을 변수를 설정해줍니다.
for a, b, c in combinations(range(m), 3):
    # combinations를 이용하여 3가지를 뽑는 조합을 만들어줍니다.
    get = 0
    for i in range(n):
        get += max(point[i][a], point[i][b], point[i][c])
    result = max(result, get)
    # 얻는 점수를 확인하여 최고값과 비교하여줍니다.

print(result)
# 최고값을 출력해줍니다.