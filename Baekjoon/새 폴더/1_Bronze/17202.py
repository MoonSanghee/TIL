A = input()
B = input()
numbers = []
for i in range(8):
    numbers.append(int(A[i]))
    numbers.append(int(B[i]))
# 주어지는 두 번호를 받고 교차로 하나의 리스트에 넣어줍니다
while len(numbers) != 2:
    new = []
    for i in range(1, len(numbers)):
        new.append((numbers[i - 1] + numbers[i]) % 10)
    numbers = new
    # 주어진 방식대로 덧셈을 반복하여 숫자가 2개가 남을때까지 반복해줍니다
print(str(numbers[0]) + str(numbers[1]))
# 요청받은 형태에 맞추어 출력하여줍니다