x, k = map(int, input().split())
# 양말의 수와 색상의 수를 받아줍니다.
socks = list(map(int, input().split()))
lefts = dict()
rights = dict()
# 양말을 받고 왼쪽 오른쪽 양말이 각각 어떤 색이 몇개씩 주어지는지 받아줍니다.
for i in range(x):
    lefts[socks[i]] = lefts.get(socks[i], 0) + 1
    rights[socks[x + i]] = rights.get(socks[x + i], 0) + 1

result = x * x
for i in lefts:
    if i in rights:
        result -= lefts[i] * rights[i]
# 좌 우 색이 다르게 짝지는 경우를 확인해줍니다.

print(result)
# 결과를 출력해줍니다.