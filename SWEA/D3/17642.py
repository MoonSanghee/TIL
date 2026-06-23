T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    A, B = map(int, input().split())
    result = 0
    # 주어지는 두 수와 결과를 담을 변수를 설정해줍니다
    if B - A == 0:
        result = 0
    elif B - A <= 1:
        result = -1
    else:
        result = (B - A) // 2
    # 두 수의 차를 확인하여 최대 조작횟수를 구해줍니다
    # 두 수의 차가 1이 아닌 홀수라면 3을 한 번 사용하고 2를 두 수가 같아질때까지 사용하면되고
    # 두 수의 차가 짝수라면 2를 두 수가 같아질때까지 사용해주면됩니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다