n = int(input())
numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
# 수열의 길이와 두 수열을 받아줍니다.
big = 0
small = 0
for i in numbers1:
    big += abs(i)

for j in numbers2:
    small += abs(j)
# 수를 뒤집는 횟수에 제한이 없으므로 가장 큰 합과 가장 작은 합은 절대값이 가장 큰 경우를 구하고 +, -로 표시하면 되니 두 수열의 절대값 합을 구해줍니다.

print(big + small)
# 두 수열의 절대값 합을 구해줍니다.