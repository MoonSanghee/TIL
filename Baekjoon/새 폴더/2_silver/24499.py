n, k = map(int, input().split())
pies = list(map(int, input().split()))
# 주어지는 파이의 개수와 먹으려는 파이의 수, 놓여있는 파이를 받아줍니다
pies += pies
# 원형 테이블에 놓여있는 파이를 한 바퀴 돌아서 값을 확인하는 경우가 있기에 2번 반복하여 리스트에 담아줍니다
result = sum(pies[:k])
check = sum(pies[:k])
# 최초 k개의 파이 합을 구해 결과값과 비교할 값에 담아줍니다
for i in range(k, n + k):
    check += pies[i]
    check -= pies[i - k]
    result = max(result, check)
    # 테이블을 순회하며 새로 먹을수있는 파이값을 더하고 못 먹게되는 파이값을 빼주어 새로 주어지는 
    # 비교값과 결과값을 비교해 갱신해줍니다

print(result)
# 결과를 출력해줍니다