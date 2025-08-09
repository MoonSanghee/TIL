n = int(input())
# 좌석의 수를 받아줍니다
arr = [1, 1, 2, 3]
# 연속한 좌석에 앉을수 있는 방법의 수를 담을 변수를 설정해줍니다
while len(arr) <= n:
    arr.append(arr[-1] + arr[-2])
# 최장 n의 사람이 연속할수 있으므로 n명까지 연속하는 경우를 리스트에 담아줍니다
m = int(input())
result = 1
last = 0
# m을 받고 결솨를 담을 변수와 마지막까지 확인한 자리를 담을 변수를 설정해줍니다

for _ in range(m):
    vip = int(input())
    result *= arr[vip - last - 1]
    last = vip
# vip의 번호를 받고 연속한 구간의 앉을수 있는 방법만큼 결과에 곱해줍니다
result *= arr[n - last]
# 마지막으로 받은 vip부터 남은 사람들의 연속하는 방법을 곱해줍니다
print(result)
# 결과를 출력해줍니다