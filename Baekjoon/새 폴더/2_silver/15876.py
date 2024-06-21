n, k = map(int, input().split())
number = []
# 두 수를 받고 전체 게임이 진행되는 순서를 담을 리스트를 만들어줍니다.
num = 0
while num < 5 * n:
    b = bin(num)
    for i in range(2, len(b)):
        number.append(b[i])
    num += 1
# 2진수를 확인하여 각 차례에 오는 수를 리스트에 담아줍니다.
jinsoo = []
for i in range(k - 1, len(number), n):
    jinsoo.append(number[i])
    if len(jinsoo) == 5:
        break
# 진수가 차례마다 말해야하는 수를 받아줍니다.
print(*jinsoo)
# 출력 조건에 맞게 출력해줍니다.