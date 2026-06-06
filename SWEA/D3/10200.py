T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    N, A, B = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    big = min(A, B)
    if N > A + B:
        small = 0
    else:
        small = A + B - N
    
    print(f'#{t + 1} {big} {small}')
    # 결과를 주어진 양식에 맞게 출력해줍니다