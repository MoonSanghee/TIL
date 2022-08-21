test = int(input())
for t in range(1, test +1):
    lines = list(map(int, input().split()))
    check = list(set(lines))
    for i in check:
        if lines.count(i) % 2 == 1:
            print(f'#{t} {i}')