N = int(input())
A = list(input().split())
B = list(input().split())
# 주어지는 수열의 길이와 두 수열을 받아줍니다
X = ''
Y = ''
for i in range(N):
    X += A[i]
    Y += B[i]
# 두 수열의 주어지는 수를 차례대로 이어줍니다
if int(X) < int(Y):
    print(int(X))
else:
    print(int(Y))
# 이어서 완성한 수를 비교하여 작은 값을 출력해줍니다