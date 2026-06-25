T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    A, B = map(int, input().split())
    # 두 수를 받아줍니다
    if A == B:
        print(f'#{t + 1} {A}')
    else:
        print(f'#{t + 1} {1}')
    # 결과를 주어진 형식에 맞게 출력해줍니다