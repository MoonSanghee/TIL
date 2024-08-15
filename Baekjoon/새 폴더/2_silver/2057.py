n = int(input())
# 찾을 수를 받아줍니다.
fact = [1, 1]

while True:
    if fact[-1] > 10 ** 18:
        break
    fact.append(fact[-1] * len(fact))
    # 주어지는 수의 범위 안을 확인하므로 10의 18승이하의 팩토리얼 값을 구해줍니다.

number = 0

for i in range(20, -1, -1):
    if number + fact[i] < n:
        number += fact[i]
    elif number + fact[i] == n:
        print("YES")
        exit()
    # 리스트에 담아둔 팩토리얼 계산값이 큰 수부터 더해서 원하는 수가 된다면 YES를 출력하고 작동을 멈추고
    # 작다면 수를 더해주고 커지면 수를 사용하지 않으며 진행해줍니다. 
print("NO")
# 모든 팩토리얼 수를 확인하고 원하는 값을 만들수없다면 NO를 출력해줍니다.