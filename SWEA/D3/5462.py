test = int(input())
for t in range(1, test + 1):
    A, B, C = map(int, input().split())
    print(f'#{t} {C // min(A, B)}')