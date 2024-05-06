n = int(input())
li = list(map(int, input().split()))
# 카드의 개수와 카드 더미를 받아줍니다.
print(sum(li) - max(li))
# 모든 수를 더하고 가장 큰 수를 뺀 값을 출력해줍니다.