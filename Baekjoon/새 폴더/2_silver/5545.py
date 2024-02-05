n = int(input())
a, b = map(int, input().split())
# 토핑의 개수와 도우, 토핑의 가격을 받아줍니다.
c = int(input())
result = c
cost = a
# 도우의 열량을 받고 열량과 비용을 담을 변수를 정해줍니다.

d = []
for _ in range(n):
    d.append(int(input()))
d.sort(reverse=True)
# 토핑의 열량을 리스트에 담고 내림차순으로 정렬해줍니다.

for i in d:
    if result / cost < i / b:
        result += i
        cost += b
# 토핑을 추가하였을때 가격대비 열량이 증가하는 토핑을 다 추가해줍니다.
print(int(result / cost))
# 가격당 열랑의 정수부분을 출력해줍니다.