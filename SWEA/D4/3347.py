T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    votes = [0] * N
    # 주어지는 변수들을 받고 각 종목의 득표를 담을 변수를 설정해줍니다
    for i in range(M):
        for j in range(N):
            if A[j] <= B[i]:
                votes[j] += 1
                break
    # 각 심사위원을 순회하며 투표할 종목을 확인하여 투표할 종목을 확인해줍니다
    result = 0
    for i in range(N):
        if votes[i] > votes[result]:
            result = i
    # 최고 득점 종목을 확인해줍니다
    print(f'#{t + 1} {result + 1}')
    # 결과를 주어진 양식에 맞게 출력해줍니다