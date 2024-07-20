n = int(input())
arr = list(map(int, input().split()))
# 근무일수와 근무를 서야하는 병사의 번호들을 받아줍니다.

d = dict()
result = 0
# 각 병사별 근무를 서야하는 날을 담을 변수와 가장 많은 근무에 들어가는 횟수를 담을 변수를 설정해줍니다.
for i in arr:
    d[i] = d.get(i, 0) + 1
    result = max(d[i], result)
# 병사들의 근무 일수를 병사 번호, 근무일을 키, 밸류값으로 가지도록 딕셔너리에 담아줍니다.
if result <= (n + 1) // 2:
    print("YES")
else:
    print("NO")
# 가장 많은 근무를 들어가는 병사가 절반 이하로 근무에 들어가는지 확인하고 결과를 출력해줍니다.