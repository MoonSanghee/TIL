result = 0
for _ in range(4):
    result += int(input())
# 4곳을 방문하는데 드는 시간을 차례로 더하여줍니다.
print(result//60)
# 60을 나눈 몫이 전부 이동하는데 걸리는 분이고
print(result%60)
# 나머지는 초가 됩니다.