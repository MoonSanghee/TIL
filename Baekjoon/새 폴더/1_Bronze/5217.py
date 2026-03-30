T = int(input())
# 테스트 케이스의 수를 받아줍니다
pairs = dict()
for i in range(1, 13):
    pair = ''
    for j in range(1, i // 2 + 1):
        if j != i - j:
            if j != 1:
                pair += ', '
            pair += str(j) + ' ' + str(i - j)
    pairs[i] = pair
# 주어지는 수의 범위가 테스트 케이스의 범위보다 주어지는 모든 수의 쌍들을 찾아 딕셔너리에 담아줍니다
for _ in range(T):
    n = int(input())
    print(f'Pairs for {n}: {pairs[n]}')
# 주어진 수를 만드는 쌍을 주어진 형식에 맞게 출력해줍니다