n = int(input())
# 주어지는 블록의 개수를 받아줍니다
floor = 0
block = 0
# 각 층별 쌓았을때 블록이 최소 몇개 필요한지 담을 변수를 설정해줍니다
while block <= n:
    block += 2 * floor ** 2 + floor * 2 + 1
    floor += 1
# 층을 더하며 안정적으로 층이 완성된다면 다음 층을 확인해줍니다
print(floor - 1)
# 멈추었을때 다음 층이 완성되지 못했으므로 층을 1뺀 값을 출력해줍니다