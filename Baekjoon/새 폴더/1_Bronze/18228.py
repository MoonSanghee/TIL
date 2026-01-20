n = int(input())
maps = list(map(int, input().split()))
# 얼음의 개수와 주어지는 상태를 받아줍니다
for i in range(n):
    if maps[i] == -1:
        l = min(maps[:i])
        r = min(maps[i + 1:])
        print(l + r)
        break
    # 펭귄의 위치를 찾아 펭귄의 앞뒤로 얼음을 깨는데 필요한 최소한의 힘을 출력해줍니다