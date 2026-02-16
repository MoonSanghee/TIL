n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 주어지는 편의점의 수와 브랜드의 수를 받고 편의점을 받아줍니다
d = dict()
# 브랜드별로 편의점이 얼마씩 있는지 담을 딕셔너리를 만들어줍니다
for i in arr:
    d[i] = d.get(i, 0) + 1
# 브랜드별 편의점이 몇개씩 있는지 구해줍니다
result = 0
# 결과를 담을 변수를 정해줍니다
for i in d:
    result = max(result, d[i])
print(result)
# 딕셔너리를 순회하며 가장 많은 브랜드를 찾아 출력해줍니다