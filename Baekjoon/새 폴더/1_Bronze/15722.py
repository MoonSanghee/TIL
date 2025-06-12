n = int(input())
need, moved, turned = 1, 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = [0, 0]

while n:
    n -= 1
    moved += 1
    result[0] += dx[turned]
    result[1] += dy[turned]
    if moved == need:
        if turned % 2 == 1:
            need += 1
        moved = 0
        turned = (turned + 1) % 4

print(*result)