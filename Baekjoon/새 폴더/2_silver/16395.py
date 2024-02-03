n, k = map(int, input().split())
# n, k를 받아줍니다.
cnt = 1
numbers = [1]
# 행의 위치와 수열을 담을 변수를 설정해줍니다.
while cnt < n:
    cnt += 1
    # 행이 내려갔음을 표시해줍니다.
    new = []
    for i in range(len(numbers) + 1):
        if i == 0 or i == len(numbers):
            new.append(1)
        else:
            new.append(numbers[i] + numbers[i - 1])
        # 행의 처음이나 마지막이라면 1을 아니라면 이웃한 두 수의 합을 리스트에 담아줍니다.
    numbers = new
    # 행의 수열을 갱신해줍니다.
print(numbers[k - 1])
# 수열에서 찾는 위치의 수를 출력해줍니다.