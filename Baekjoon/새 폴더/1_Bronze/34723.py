p, m, c = map(int, input().split())
x = int(input())
# 주어지는 변수들을 받아줍니다
result = float('inf')
# 결과를 담을 변수를 설정해줍니다
for i in range(1, p + 1):
    for j in range(1, m + 1):
        for k in range(1, c + 1):
            result = min(result, abs((i + j) * (j + k) - x))
# 주어진 변수 이하의 모든 정수를 순회하며 최소값을 찾아줍니다
print(result)
# 결과를 출력해줍니다