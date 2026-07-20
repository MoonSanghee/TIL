T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    first = input()
    second = input()
    # 주어지는 두 문자열을 받아줍니다
    d = dict()
    result = first[0]
    for i in first:
        d[i] = 0
    # 딕셔너리에 첫 문자열에 포함된 문자들을 넣어줍니다
    for i in second:
        if i in d:
            d[i] += 1
    # 두 번째 문자열을 순회하며 첫번째 문자열에 포함된 문자의 개수를 확인해줍니다
    for i in first:
        if d[i] > d[result]:
            result = i
    # 가장 많이 사용된 문자를 찾아줍니다
    print(f'#{t + 1} {d[result]}')
    # 결과를 출력해줍니다