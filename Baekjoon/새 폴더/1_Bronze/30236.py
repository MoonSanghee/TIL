t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    new = [0] * n
    # 수열의 길이와 a 수열을 받고 b수열을 담을 변수를 설정해줍니다
    if numbers[0] == 1:
        new[0] = 2
    else:
        new[0] = 1
    # b수열의 0번 인덱스 값을 담아줍니다
    for i in range(1, n):
        new[i] = new[i - 1] + 1
        if numbers[i] == new[i]:
            new[i] += 1
    # 수열의 값을 체워줍니다
    print(new[-1])
    # bn의 마지막 값을 출력해줍니다