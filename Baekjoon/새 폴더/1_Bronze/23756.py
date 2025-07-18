n = int(input())
# 맞춰야하는 노브의 개수를 받아줍니다
start = int(input())
# 초기 노브 각도를 받아줍니다
result = 0
# 돌린 노브의 각도 합을 담을 변수를 설정해줍니다
for _ in range(n):
    target = int(input())
    # 맞추려는 노브를 받아줍니다
    result += min(abs(start - target), 360 - abs(start - target))
    start = target
    # 좌우중에 적게 이동하는 법을 찾아 합으로 더하고 시작 노브의 각도를 갱신해줍니다
print(result)
# 결과값을 출력해줍니다