h, w = map(int, input().split())
n = int(input())
stickers = [list(map(int, input().split())) for _ in range(n)]
# 주어지는 영역의 크기를 받고 스티커의 개수와 스티커의 크기들을 받아줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        size = r1 * c1 + r2 * c2
        # 2개의 스티커를 차례대로 선택하고 두 스티커가 영역안에 들어가면 덮어지는 사이즈를 구해줍니다
        if (r1 + r2 <= h and max(c1, c2) <= w) or (r1 + r2 <= w and max(c1, c2) <= h):
            result = max(result, size)
        # 두 스티커를 주어진대로 나란히 놓았을때 주어진 영역에 들어가는지 확인해줍니다
        elif (r1 + c2 <= h and max(c1, r2) <= w) or (r1 + c2 <= w and max(c1, r2) <= h):
            result = max(result, size)
        # 2번째 스티커를 90도 돌려 나란히 놓았을때 주어진 영역에 들어가는지 확인해줍니다
        elif (c1 + r2 <= h and max(r1, c2) <= w) or (c1 + r2 <= w and max(r1, c2) <= h):
            result = max(result, size)
        # 1번째 스티커를 90도 돌려 나란히 놓았을때 주어진 영역에 들어가는지 확인해줍니다
        elif (c1 + c2 <= h and max(r1, r2) <= w) or (c1 + c2 <= w and max(r1, r2) <= h):
            result = max(result, size)
        # 두 스티커를 모두 90도 돌려 나란히 놓았을때 주어진 영역에 들어가는지 확인해줍니다
print(result)
# 결과를 출력해줍니다