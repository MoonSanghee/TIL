test = int(input())
for t in range(1, test + 1):
    choiso, choidae, siljae = map(int, input().split())
    if siljae > choidae:
        print(f'#{t} {-1}')
    elif choiso > siljae:
        print(f'#{t} {choiso - siljae}')
    else:
        print(f'#{t} {0}')