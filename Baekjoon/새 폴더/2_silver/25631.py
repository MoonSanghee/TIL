n = int(input())
dolls = list(map(int, input().split()))
# 인형의 개수와 인형의 크기들을 받아줍니다.
d = dict()
result = 0

for i in dolls:
    d[i] = d.get(i, 0) + 1
    result = max(d[i], result)
# 각 인형의 크기별로 몇개씩 있는지 담고 가장 많은 인형이 몇개인지 확인해줍니다.
print(result)
# 결과를 출력해줍니다.