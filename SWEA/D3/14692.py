T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    # 나무의 길이를 받아줍니다
    if n % 2:
        print(f'#{t + 1} Bob')
    else:
        print(f'#{t + 1} Alice')
    # 나무의 길이가 짝수라면 홀수번 자를수 있으므로 먼저 시작하는 앨리스가 이기고 짝수라면 반대이므로 결과를 주어진 양식에 맞춰 출력해줍니다