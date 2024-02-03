n, k = list(map(int, input().split()))
numbers = list(map(int, input().split(',')))
# n, k, 수열을 받아줍니다.
cnt = 0
# 인접한 원소의 차이를 확인한 수를 기록할 변수를 만들어줍니다.
while cnt < k:
    cnt += 1
    com = []
    for i in range(1, len(numbers)):
        com.append(numbers[i] - numbers[i - 1])
    numbers = com
    # 차를 확인하여 리스트에 넣어주고 확인이 끝난후 수열 numbers를 갱신해줍니다.
result = f'{numbers[0]}'
for i in range(1, len(numbers)):
    result += ',' + str(numbers[i])

print(result)
# 수열을 출력해줍니다.