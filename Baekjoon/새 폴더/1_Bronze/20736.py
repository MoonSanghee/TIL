a, b = map(int, input().split())
k, x = map(int, input().split())
cnt = 0
# 주어지는 두 범위와 친구가 될수있는 사람의 수를 담을 변수를 설정해줍니다

for i in range(a, b + 1):
    if k - x <= i <= k + x:
        cnt += 1
# 친구가 될 수 있는사람을 확인해 추가해줍니다
if cnt == 0:
    print("IMPOSSIBLE")
else:
    print(cnt)
# 친구의 수에 따라 주어진 형식에 맞춰 출력해줍니다