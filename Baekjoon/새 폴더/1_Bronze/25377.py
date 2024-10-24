n = int(input())
result = 1001
# 빵집의 수와 최대 시간보다 큰 수를 결과로 설정해줍니다.
for _ in range(n):
    A, B = map(int, input().split())
    if B >= A:
        result = min(result, B)
    # 빵을 살 수 있고 값이 갱신되는지 확인하여 result값을 갱신해줍니다.

if result == 1001:
    print(-1)
else:
    print(result)
    # result값이 갱신된적 없으면 -1있으면 갱신된 값을 출력해줍니다.