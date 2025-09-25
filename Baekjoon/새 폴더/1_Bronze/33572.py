n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
for i in range(n):
    m -= (arr[i] - 1)
# 친구들의 순서를 바꿀수 있으므로 모든 친구들과 보낼수 있는 최대 시간만큼 m에서 빼줍니다
if m > 0:
    print("OUT")
else:
    print("DIMI")
# m이 양수라면 보낼 시간이 더 필요하므로 사랑에 빠지게되고 아니라면 사랑에 빠지지 않을수 있습니다