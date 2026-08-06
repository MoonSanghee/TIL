n = int(input())
result = [1, 1]
# 주어지는 수열의 길이를 받고 피보나치 수열을 담을 리스트를 만들어줍니다
while len(result) < n:
    result.append(result[-1] + result[-2])
# 주어진 길이가 되도록 연산을 진행해줍니다
if n == 1:
    print([1])
else:
    print(result)
# 만들어진 수열을 출력해줍니다