n = int(input())
maps = list(map(int, input().split()))
maps.sort()
if n % 2 == 1:
    print(maps[n // 2])
else:
    print(maps[(n // 2) - 1])
# 혹은 print(maps[(n - 1) // 2])로 표현하면 숫자가 몇 개 주어졌는지 확인 안 해도 괜찮다.