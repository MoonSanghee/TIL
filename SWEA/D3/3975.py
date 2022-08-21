test = int(input())
result = []
for t in range(1, test + 1):
    a, b, c, d = map(int, input().split())
    ALICE = a/b
    BOB = c/d
    if ALICE == BOB:
        result.append(f'#{t} DRAW')
    elif ALICE > BOB:
        result.append(f'#{t} ALICE')
    else:
        result.append(f'#{t} BOB')

for i in result:
    print(i)