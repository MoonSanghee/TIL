import sys
input=sys.stdin.readline

n = int(input())
# 테스트 케이스의 수를 받아줍니다,
def check(x):
    for i in range(2,int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
# 정수의 제곱근까지 정수가 나누어 떨어지는 수가 있는지 확인하는 함수를 구현해줍니다.(소수인지 확인)

for i in range(n):
    num = int(input())
    # 확인할 수를 받아줍니다.
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        # 입력받은 수가 0이나 1이라면 2를 출력해줍니다.
        if check(num):
            print(num)
            break
        else:
            num += 1
        # 이외의 수라면 입력받은 수부터 소수인지 확인하고 아니라면 소수가 나올때까지 1을 더하여 확인을 반복해줍니다.