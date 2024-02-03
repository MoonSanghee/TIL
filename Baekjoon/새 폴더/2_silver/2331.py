n, m = map(int, input().split())
# 두 정수를 받아줍니다.
numbers = [n]
# 시작하는 수를 리스트에 넣어줍니다.
while True:
    number = str(numbers[-1])
    # 마지막 수를 받아줍니다.
    new = 0
    for i in number:
        new += int(i) ** m
    # 마지막 수의 각 자리의 m제곱값을 new에 더해줍니다.
    if new in numbers:
        break
    # new가 반복된다면 확인을 멈춥니다.
    numbers.append(new)
    # 처음 만들어졌다면 리스트에 새로 만들어진 수를 넣습니다.

print(numbers.index(new))
# 반복이 시작되는 자리를 찾아 출력해줍니다.