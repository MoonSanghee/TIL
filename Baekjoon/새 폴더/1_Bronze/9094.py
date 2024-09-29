t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    n, m = map(int, input().split())
    # 주어지는 두 수를 받아줍니다
    cnt = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            if (i * i + j * j + m) % (i * j) == 0:
                cnt += 1
    # 주어진 수 사이의 두 수를 확인하며 주어진 조건에 맞는 수가 몇 쌍 있는지 찾아줍니다.
    print(cnt)
    # 결과를 출력해줍니다.