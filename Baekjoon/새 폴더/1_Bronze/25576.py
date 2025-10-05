n, m = map(int, input().split())
# 주어지는 스트리머의 수와 시청자수 변화 추이의 수를 받아줍니다
l = list(map(int, input().split()))
# 첫 스트리머의 기록을 받아줍니다
cnt = 0
# 사이가 좋지 않은 스트리머의 수를 담을 변수를 정해줍니다
for _ in range(n - 1):
    k = list(map(int, input().split()))
    total = 0

    for i in range(m):
        total += abs(l[i] - k[i])
    
    if total > 2000:
        cnt += 1
    # 다른 스트리머들과 비교하며 사이가 나쁜 스트리머의 수를 확인해줍니다
if n - 1 <= cnt * 2:
    print("YES")
else:
    print("NO")
# 악질인지 확인하여 결과를 출력해줍니다