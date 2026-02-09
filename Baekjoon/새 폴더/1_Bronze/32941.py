t, x = map(int, input().split())
n = int(input())
# 예약할 수 있는 교시의 수와 예약한 교시, 조원의 수를 받아줍니다
flag = True
# 모든 조원이 참여가능한지 확인할 변수를 설정해줍니다
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    if x not in arr:
        flag = False
    # 주어지는 조원의 참여 가능 교시들을 받고 예약한 교시가 포함되어있는지 확인해줍니다

if flag: print("YES")
else: print("NO")
# 결과를 출력해줍니다