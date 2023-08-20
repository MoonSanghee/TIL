n = int(input())
# 케이스의 수를 받아줍니다.
for i in range(n):
    num = sum(list(map(int, input().split())))
    # 두 수의 합을 구해줍니다.
    print(f'Case {i + 1}: {num}')
    # 출력 형식에 맞추어 출력해줍니다.