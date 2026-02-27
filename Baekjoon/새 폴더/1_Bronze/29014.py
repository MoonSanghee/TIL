n = int(input())
tops = list(map(int, input().split()))
# 첨탑의 개수와 놓여있는 탑의 상태를 받아줍니다
result = 1
last = tops[0]
# 넘어뜨리는 횟수를 담을 변수를 만들고 마지막 탑으로 가장 앞에 위치한 탑을 설정해줍니다
for i in range(1, n):
    if tops[i] >= last:
        result += 1
    # 이전 탑보다 낮지 않다면 넘어뜨리는 횟수를 추가해줍니다
    last = tops[i]
    # 마지막 탑의 값을 갱신해줍니다

print(result)
# 결과를 출력해줍니다