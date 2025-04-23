n = int(input())
numbers = set()
# 확인하고자하는 수를 받고 구구단에 등장하는 모든 수를 담을 셋을 만들어줍니다
for i in range(1, 10):
    for j in range(2, 10):
        number = i * j
        numbers.add(i)
        numbers.add(j)
        numbers.add(number)
# 2단부터 9단까지 등장하는 모든 수를 셋에 넣어줍니다
if n in numbers:
    print(1)
else:
    print(0)
# 찾는 수가 존재하는지 확인하여 결과를 출력해줍니다