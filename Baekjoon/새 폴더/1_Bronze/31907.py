n = int(input())
# 주어지는 변수를 받아줍니다
for i in range(3):
    for _ in range(n):
        if i == 0:
            print('G' * n + '.' * (n * 3))
        elif i == 1:
            print('.' * n + 'I' * n + '.' * n + 'T' * n)
        else:
            print('.' * (n * 2) + 'S' * n + '.' * n)
# 요청받은 형식에 맞게 결과를 출력해줍니다