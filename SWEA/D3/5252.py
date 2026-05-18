T = int(input())
# 주어지는 테스트케이스의 개수를 받아줍니다
for t in range(T):
    A, B = map(int, input().split())
    N = [input() for _ in range(A)]
    # 주어지는 단어의 수와 A를 받아줍니다
    result = 0
    # 공통 단어의 수를 담을 변수를 설정해줍니다
    for _ in range(B):
        word = input()
        if word in N:
            result += 1
    # B를 순회하며 공통 단어인지 확인해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞춰 출력해줍니다