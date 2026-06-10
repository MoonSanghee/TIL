T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    N, S = input().split()
    N = int(N)
    result = 0
    # 주어지는 단어의 길이와 단어를 받고 결과를 담을 변수를 설정해줍니다
    for i in range(N):
        A, C = 0, 0
        for j in range(i, N):
            if S[j] == 'A':
                A += 1
            elif S[j] == 'T':
                A -= 1
            elif S[j] == 'C':
                C += 1
            else:
                C-= 1
            if A == 0 and C == 0:
                result += 1
    # 주어진 단어의 모든 구간을 순회하며 모든 반전 관계의 문자들을 찾아줍니다
    print(result)
    # 결과를 출력해줍니다