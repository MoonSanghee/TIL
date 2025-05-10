T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    A, n = map(int, input().split())
    # 주어지는 변수를 받아줍니다
    result = []
    while A:
        result.append(A % n)
        A //= n
    # A를 n으로 나눈 나머지를 받아 A를 n진법으로 바꾼 수를 뒤집은 값을 구해줍니다
    if result == result[::-1]:
        print(1)
    else:
        print(0)
    # 회문인지 확인하고 결과를 출력해줍니다