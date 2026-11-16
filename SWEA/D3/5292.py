T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    # 주어지는 변수들을 받아줍니다
    print(f'#{tc} {len(A) + len(B) - len(A.union(B))}')
    # 중복되는 수의 개수를 확인하여 출력해줍니다