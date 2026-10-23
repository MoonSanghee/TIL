from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    # 주어지는 선수의 수를 받아줍니다 
    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))
    # 각 팀의 선호 순서를 받아줍니다
    result = [''] * N
    # 각선수가 뽑힌 팀을 담을 변수를 설정해줍니다
    while A or B:
        while A:
            if result[A[0] - 1] == '':
                x = A.popleft() - 1
                result[x] = 'A'
                break
            else:
                A.popleft()
        while B:
            if result[B[0] - 1] == '':
                y = B.popleft() - 1
                result[y] = 'B'
                break
            else:
                B.popleft()
        # 양 팀이 번갈아가며 선수를 뽑아줍니다
    print(''.join(result))
    # 결과를 주어진 양식에 맞게 출력해줍니다