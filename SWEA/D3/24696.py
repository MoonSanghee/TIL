T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    A, B ,C = map(int, input().split())
    # 주어지는 세 변의 길이를 받아줍니다
    if ((A * B * C) - 1) % 2:
        print(1)
    else:
        print(2)
    # 자를수 있는 수를 확인하여 승자를 출력해줍니다