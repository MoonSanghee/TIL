import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
# 세 변의 합의 길이와 만들수 있는 조합의 수를 담을 변수를 만들어줍니다.
for i in range(1, n + 1):
    for j in range(i, n + 1):
        # n길이 이하의 가장 긴 변을 제외한 두 변의 길이를 설정해줍니다.
        k = n - i - j
        # 나머지 한 변의 길이를 설정해줍니다.
        if k >= i + j:
            continue
        # 삼각형이 성립하지 않으면 다음 조합을 확인합니다.
        else:
            if j > k:
                break
            cnt += 1
            # k가 가장 큰 변이라면 cnt에 값을 더해주고 K보다 큰 변이 있으면 현재 i의 길이에서 남은 조합을 건너뜁니다.

print(cnt)
# cnt에 담긴 값을 출력해줍니다