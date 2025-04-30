def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)
# 서로소를 구하기위해 최대공약수와 최소공배수를 구하는 함수를 설정해줍니다
N = int(input())
A = list(map(int, input().split()))
X = int(input())
# 주어지는 변수들을 받아줍니다
numbers = []
for i in range(N):
    if A[i] != X:
        if gcd(A[i], X) == 1:
            numbers.append(A[i])
# 서로소를 구하여 리스트에 모아줍니다
print('{:6f}'.format(sum(numbers)/len(numbers)))
# 주어진 자릿수까지 맞추어 출력하여줍니다