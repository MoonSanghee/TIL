n = int(input())
arr = list(map(int, input().split()))
# 주어지는 일수와 각 일별 푼 문제의 수를 받아줍니다
result = 0
now = 0
# 최장 스트릭과 현재 스트릭을 담을 변수를 설정해줍니다
for i in arr:
    if i == 0:
        result = max(result, now)
        now = 0
    else:
        now += 1
    # 문제를 풀지 않았다면 현재 스트릭과 최장 스트릭을 비교하여 갱신해주고 풀었다면 스트릭을 증가시켜줍니다
result = max(result, now)
print(result)
# 반복이 끝난다음 최장 스트릭을 한 번 더 확인 후 결과를 출력해줍니다