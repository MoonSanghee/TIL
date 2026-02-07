n = int(input())
m = int(input())
# 주어지는 시간과 최초 터널에 있는 차의 수를 받아줍니다
result = m
flag = True
# 최대 차량의 수와 0아래로 내려가는지를 확인하기위한 변수를 설정해줍니다
for _ in range(n):
    i, o = map(int, input().split())
    m = m + i - o
    # 들어가고 나가는 차의 수를 받아 계산을 진행해줍니다
    if m < 0:
        flag = False
    result = max(m, result)
    # 차량이 0아래로 내려갔는지 확인하고 최대 차량의 수를 갱신해줍니다

if flag:
    print(result)
else:
    print(0)
# 결과를 출력해줍니다