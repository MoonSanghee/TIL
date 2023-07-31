n = int(input())
# 버튼을 누른 횟수를 받아줍니다.
a, b = 1, 0
# a와 b의 기본값을 설정해줍니다.
for i in range(n):
    a, b = b, a + b
print(a, b)