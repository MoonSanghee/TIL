n = int(input())
machines = list(map(int, input().split()))
machines.sort()
# 기구의 개수를 받고 기구들의 정보를 받은 뒤 오름차순으로 정렬해줍니다.
result = machines[-1]
# 최소 근손실을 맨 뒤의 기구 값으로 설정해줍니다.
if n % 2 == 1:
    for i in range(n // 2):
        lose = machines[i] + machines[n - i - 2]
        result = max(result, lose)
    # 홀수라면 맨 뒤의 기구는 마지막날에 PT를 받으므로 맨 처음부터 오름차순과 맨 뒤에서 두번째부터 내림차순 기구를 짝지어 PT를 받을때 발생하는 근손실을 확인해줍니다.
else:
    for i in range(n // 2):
        lose = machines[i] + machines[n - i - 1]
        result = max(result, lose)
    # 짝수라면 1개의 기구만 PT 받는 경우가 없으므로 맨 처음 기구와 맨 마지막 기구부터 각각 오름차순, 내림차순으로 매칭하며 최대 근손실을 확인해줍니다.

print(result)
# 결과값을 출력해줍니다.