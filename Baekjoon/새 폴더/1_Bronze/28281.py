n, x = map(int, input().split())
price = list(map(int, input().split()))
# 주어지는 날과 사려는 양말의 수, 날 별 양말의 가격을 받아줍니다
result = 2000000
# 연속한 이틀간의 가격이 가장 작은 값을 담을 변수를 설정해줍니다
for i in range(1, n):
    result = min(result, price[i] + price[i - 1])
# 연속한 이틀을 선회하며 최소값을 출력해줍니다
print(result * x)
# 찾은 최소값에 필요한 양말의 수를 곱한 결과를 출력해줍니다