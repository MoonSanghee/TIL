T = int(input())

tiles = [0, 1, 3, 6]

while len(tiles) < 31:
    tiles.append(tiles[-1] + tiles[-2] * 2 + tiles[-3])

for tc in range(1, T + 1):
    n = int(input())
    print(f'#{tc} {tiles[n]}')