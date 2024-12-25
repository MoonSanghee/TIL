t = int(input())
# 테스트케이스의 수를 받아줍니다
for tc in range(t):
    a = input()
    b = input()
    # 두 단어를 받아줍니다
    d = dict()
    for i in a:
        d[i] = d.get(i, 0) + 1
    for i in b:
        d[i] = d.get(i, 0) - 1
    # 두 단어를 순회하며 문자 개수의 차이를 딕셔너리에 담아줍니다
    
    cnt = 0
    for i in d:
        cnt += abs(d[i])
    # 두 단어의 다른 문자수를 구해줍니다
    print(f'Case #{tc + 1}: {cnt}')
    # 주어진 형식에 맞게 출력해줍니다