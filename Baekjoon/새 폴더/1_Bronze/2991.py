a, b, c, d = map(int, input().split())
deliveries = list(map(int, input().split()))
# 개가 활동하는 시간과 배달이 오는 시간을 받아줍니다
for i in deliveries:
    result = 0
    if 0 <= i % (a + b) <= a:
        result += 1
    if 0 <= i % (c + d) <= c:
        result += 1
    # 각 배달이 올 때 두 개가 각각 활동중인지 확인해줍니다
    print(result)
    # 결과를 출력해줍니다