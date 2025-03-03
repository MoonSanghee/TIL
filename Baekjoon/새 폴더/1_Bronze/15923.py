n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
# 주어지는 좌표의 수와 좌표를 받아줍니다
print((max(x) - min(x) + max(y) - min(y)) * 2)
# 둘레를 구하므로 x, y축에서 각각 가장 큰 값에서 가장 작은 값 차를 구하고 2를 곱한 값을 출력해줍니다