T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    n = int(input())
    # 주어지는 정수를 받아줍니다
    check = 10
    while check < n:
        check *= 10
    # n의 제곱수의 끝자리를 확인하기 위해 나눌 10의 제곱수를 구해줍니다
    if (n * n) % check == n:
        print("YES")
    else:
        print("NO")
    # 자기복제수인지 확인한 결과를 출력해줍니다