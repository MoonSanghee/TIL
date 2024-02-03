n = int(input())
# 손님의 수를 받아줍니다.
customers = []
for _ in range(n):
    customers.append(int(input()))
# 손님이 지급하려는 팁을 받아줍니다.
customers.sort(reverse=True)
# 주려는 팁을 기준으로 내림차순으로 정렬해줍니다
result = 0
# 최종적으로 받을 팁을 담을 변수를 지정해줍니다.
for i in range(n):
    tip = customers[i] - i
    # 실제로 받을 팁을 구해줍니다.
    if tip > 0:
        result += tip
    else:
        break
    # 팁이 양수라면 result에 더해주고 아니라면 확인을 멈추어줍니다.

print(result)
# 최종적으로 받을 팁을 출력해줍니다.