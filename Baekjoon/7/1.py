# 7-1 문제번호 1712

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    print(A//(C - B) + 1)
