T = int(input())
# 테스트케이스의 개수를 받아줍니다
tile = [1, 3, 5]
while len(tile) != 30:
    tile.append(tile[-1] + tile[-2] * 2)
# 타일의 길이별 조합수를 구해줍니다
for t in range(T):
    N = int(input())
    N //= 10
    # 주어지는 길이를 받아줍니다
    print(f'#{t + 1} {tile[N - 1]}')
    # 결과를 주어진 양식에 맞게 출력해줍니다