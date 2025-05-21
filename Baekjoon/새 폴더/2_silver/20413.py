n = int(input())
S, G, P, D = list(map(int, input().split()))
grade = input()
# 주어지는 변수들을 받아 각 등급별 필요한 과금 제한 금액과 결제한 기간동안의 등급을 받아줍니다
result = 0
previous = 0
# 결과와 직전 달의 과금을 담을 변수를 설정해줍니다
for i in range(n):
    if grade[i] == 'B':
        result += S - 1 - previous
        previous = S - 1 - previous
    elif grade[i] == 'S':
        result += G - 1 - previous
        previous = G - 1 - previous
    elif grade[i] == 'G':
        result += P - 1 - previous
        previous = P - 1 - previous
    elif grade[i] == 'P':
        result += D - 1 - previous
        previous = D - 1 - previous
    # 다이아 등급이 아닌 각 등급이 되기 위해서는 다음 등급의 제한 한도까지 돈을 썼다고 결과에 더해주고 전 달 사용금을 바꿔줍니다
    else:
        result += D
        previous = D

print(result)
# 결과를 출력해줍니다