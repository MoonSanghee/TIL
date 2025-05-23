n = int(input())
mascot = input()
k = int(input())
# 주어지는 변수들을 받아줍니다
if mascot == 'induck':
    if k % 2 == 1:
        k += 1
else:
    if k % 2 == 0:
        k += 1
# 마스코트를 확인하여 이용할 수 있는 가장 가까운 층으로 올라가줍니다
if k > n:
    k -= 2
# 범위를 벗어났다면 2층 내려가줍니다
print(k)
# 결과를 출력해줍니다