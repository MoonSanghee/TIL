n = int(input())
# 정수를 받아줍니다
print('@' * ( n + 2))
for _ in range(n):
    print('@' + ' ' * n + '@' )
print('@' * ( n + 2))
# 결과를 출력해줍니다