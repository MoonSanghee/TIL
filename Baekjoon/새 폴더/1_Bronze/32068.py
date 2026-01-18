n = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(n):
    l, r, s = map(int, input().split())
    # 주어지는 좌표들을 받아줍니다
    print(min((r - s) * 2, (s - l) * 2 + 1))
    # 놀이가 끝나는 시점을 출력해줍니다