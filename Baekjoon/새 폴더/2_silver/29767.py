n, k = map(int, input().split())
A = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
B = [0] * n
B[0] = A[0]
for i in range(1, n):
    B[i] = B[i - 1] + A[i]
# 각 교실까지 방문하였을때 누적 값이 가장 큰 경우를 담을 리스트를 만들고 첫 번째 교실을 방문하지 않을수 
# 없으므로 첫 누적값을 첫 교실의 값으로 넣어줍니다
B.sort(reverse = True)
print(sum(B[:k]))
# 누적값을 내림차순 정렬하여 가장 값이 큰 k개의 합을 출력해줍니다