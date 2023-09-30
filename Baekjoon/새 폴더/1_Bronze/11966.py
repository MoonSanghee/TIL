numbers = [1]
number = 1
cnt = 0
while cnt < 30:
    numbers.append(number)
    number *= 2
    cnt += 1
# 1부터 2의 30승까지의 수를 리스트에 넣어줍니다.
n = int(input())
# 확인할 값을 받아줍니다.
if n in numbers:
    print(1)
else:
    print(0)
# 2의 배수라면 1을 아니면 0을 출력해줍니다.