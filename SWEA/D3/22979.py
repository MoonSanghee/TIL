T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    S = input()
    # 주어지는 문자열을 받아줍니다
    K = int(input())
    numbers = list(map(int, input().split()))
    # 주어지는 이동의 개수와 이동정보를 받아줍니다
    move = sum(numbers)
    move %= len(S)
    # 최종 이동해야하는 결과를 구해줍니다
    result = S[move:] + S[:move]
    print(result)
    # 이동한 결과 만들어진 문자열을 출력해줍니다