n = int(input())
# 주어지는 수열의 길이를 받아줍니다
result = [i + 1 for i in range(n - 1)] + [53]
# n - 1개의 수열을 각 Ai의 자리에 i + 1값을 넣어주고 최대 길이인 50보다 큰 소수를 마지막에 n길이 수열을 만들어줍니다
print(n)
print(*result)
# 수열의 길이와 수열을 출력해줍니다