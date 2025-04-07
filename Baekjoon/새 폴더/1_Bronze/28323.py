n = int(input())
numbers = list(map(int, input().split()))
# 주어지는 수열의 길이와 수열을 받아줍니다
result = 1
last = numbers[0] % 2
# 가장 앞에 위치한 수가 홀수인지 짝수인지 담아두고 수열의 길이를 1로 설정해줍니다
for i in range(n):
    if numbers[i] % 2 != last:
        last = numbers[i] % 2
        result += 1
# 홀짝이 바뀔때마다 지난 값이 무엇인지 표시하고 수열의 길이를 갱신해줍니다
print(result)
# 가장 긴 불안정한 수열의 길이를 출력해줍니다