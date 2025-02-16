n = int(input())
m = int(input())
x = list(map(int, input().split()))
# 주어지는 영역의 길이와 설치할 가로등의 개수, 가로등이 설치될 위치를 받아줍니다
result = max(x[0], n - x[-1])
# 최초 높이값으로 가장 앞쪽에 설치되는 가로등이 왼쪽을 비춰야하는 영역과 
# 가장 뒤에 설치되는 가로등이 비춰야하는 오른쪽의 영역중 큰 값으로 설정해줍니다
for i in range(1, m):
    between =  x[i] - x[i - 1] 
    
    if between > result * 2:
        result = (between + 1) // 2
# 가로등 사이 간격이 이전 높이로 충분하지 않다면 값을 갱신해줍니다
print(result)
# 결과값을 출력해줍니다