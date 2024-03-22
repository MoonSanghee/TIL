s, k = map(int, input().split())
# 두 정수를 받아줍니다.
li = [s // k for _ in range(k)]
for i in range(s % k):
    li[i] += 1
# k개의 정수를 더해 s가 되는 값중 곱했을때 가장 큰 값은 정수들의 차가 가장 적은 경우이기에 
# s를 k로 나눈 수를 k개 나머지 만큼은 그 수에 1을 더해줍니다.
result = 1
for n in li:
    result *= n
# 1에 k개의 정수를 곱해줍니다.
print(result)
# 곱한 결과값을 출력해줍니다.