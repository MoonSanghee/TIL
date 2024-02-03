t = int(input())
# 테스트의 수를 받아줍니다.
for _ in range(t):
    n, k = map(int, input().split())
    # 사탕의 개수와 만족하기위해 필요한 사타의 개수를 받아줍니다.
    cnt = 0
    # 몇 명을 초대할 수 있는지 담을 변수를 정해줍니다.
    candies = list(map(int, input().split()))
    for candy in candies:
        cnt += candy // k
        # 각 종류의 사탕마다 만족시킬수 있는 사람의 수를 더해줍니다. 
    print(cnt)
    # 초대할 수 있는 사람의 수를 출력해줍니다.