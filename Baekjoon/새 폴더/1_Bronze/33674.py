n, d, k = map(int, input().split())
s = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
most = max(s)
cycle = k // most
# 청소를 할 때 모든 지점의 별을 청소하므로 가장 많이 쌓이는 지점을 확인하여 청소 주기를 확인해줍니다
if d % cycle:
    print(d // cycle)
else:
    print(d // cycle - 1)
    # 청소 주기가 몇 번 돌아오는지 확인하여 결과를 출력해줍니다