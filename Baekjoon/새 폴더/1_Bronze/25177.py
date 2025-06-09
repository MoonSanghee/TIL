n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 현재 시설의 수와 예전 시설의 수를 받고 각 장소들의 점수를 차례대로 리스트에 담아줍니다
result = 0
# 증가된 점수의 합을 담을 변수를 설정해줍니다
if n >= m:
    for i in range(m):
        result = max(result, b[i] - a[i])
    #현재 시설이 예전 시설 이전이라면 바꾸었을때 증가되는 최대점수를 찾아줍니다
else:
    for i in range(n):
        result = max(result, b[i] - a[i])
    for i in range(n, m):
        result = max(result, b[i])
    # 예전 시설이 더 많았다면 현재 시설 수만큼 바꾸어서 증가되는 점수를 확인하고 예전에만 있었던 장소를 추가하여 증가되는 점수도 확인해줍니다

print(result)
# 결과를 출력해줍니다