n = int(input())
flag = True
# 주어지는 수를 받고 소수인지 확인한 값을 담을 변수를 설정해줍니다
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        flag = False
        break
# 주어진 수의 제곱근까지 나누어 떨어지는 수가 존재하는지 확인해줍니다
if flag:
    print('소수입니다.')
else:
    print('소수가 아닙니다.')
# 주어진 수가 소수인지 출력해줍니다