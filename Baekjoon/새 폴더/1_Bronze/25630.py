n = int(input())
N = input()
result = 0
# 주어지는 단어의 길이와 단어를 받아줍니다
for i in range(n // 2):
    if N[i] != N[n - 1 - i]:
        result += 1
# 바꾸어야하는 횟수를 확인해줍니다
print(result)
# 결과를 출력해줍니다