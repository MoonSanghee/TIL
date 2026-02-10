M = list(map(int, input().split()))
result = 0
# 분위별 장학금을 받고 결과를 담을 변수를 설정해줍니다
n = int(input())
# 재학생의 수를 받아줍니다
for _ in range(n):
    B, L, S = input().split()
    if int(S) >= 17 and float(L) >= 2.0:
        result += M[int(B)]
# 장학금 요건에 충족하면 장학금을 누적해줍니다
print(result)
# 결과를 출력해줍니다