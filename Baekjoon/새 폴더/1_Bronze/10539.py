n = int(input())
numbers = list(map(int, input().split()))
result = [numbers[0]]
# 수의 개수와 수열을 받고 답을 담을 리스트를 만들어 0번 인덱스 값을 넣어줍니다.
for i in range(1, n):
    result.append(numbers[i] * (i + 1) - sum(result))
# 이후 인덱스 자릿값들을 확인하여 차례대로 값을 구해 result리스틑에 넣어줍니다.
print(*result)
# 리스트에 담아둔 값들만 출력해줍니다.