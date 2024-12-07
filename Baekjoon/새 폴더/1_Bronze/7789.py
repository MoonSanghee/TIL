n1, x = input().split()
n2 = int(x + n1)
n1 = int(n1)
# 원래 전화번호와 더할 수를 받고 새로 만들어진 전화번호를 만들어줍니다
for i in range(2, int(n2 ** 0.5) + 1):
    if n1 % i == 0 or n2 % i == 0:
        print("No")
        break
else:
    print("Yes")
# 더 큰 수인 새로 만들어진 전화번호의 제곱근까지 순회하며 기존 전화번호와 새로 만들어진 전화번호 모두 소수인지 확인하여 조건에 맞게 출력해줍니다