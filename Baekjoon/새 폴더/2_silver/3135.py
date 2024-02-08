a, b = map(int, input().split())
# 시작과 목표 주파수를 받아줍니다.
result = abs(a - b)
# 주어진 주파수로 변경하는데 필요한 버튼수를 구해줍니다.
for _ in range(int(input())):
    k = int(input())
    if result > abs(k - b):
        result = abs(k - b) + 1
        # 즐겨찾기 주파수가 더 적은 버튼을 누르고 목표 주파수로 도달할 수 있는지 확인해줍니다.

print(result)
# 최소 버튼수를 출력해줍니다.