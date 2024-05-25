t = int(input())
# 테스트케이스의 수를 받아줍니다.
for _ in range(t):
    numbers = list(map(int, input().split()))
    # 주어지는 수열을 받아줍니다.
    n = numbers[0]
    soliders = numbers[1:]
    # 땅의 수와 병사를 나누어줍니다.
    d = dict()
    for i in soliders:
        d[i]= d.get(i, 0) + 1
    # 각 병사가 몇명 존재하는지 딕셔너리에 담아줍니다.
    end = False
    result = 0
    # 전쟁이 끝났는지와 몇번 군대가 점령하였는지 담을 변수를 설정해줍니다.
    for i in d:
        if d[i] > n / 2:
            end = True
            result = i
    # 과반을 넘는 군대가 있%다면 전쟁이 끝났다는것을 표시하고 몇번 군대가 점령했는지 값을 담아줍니다.
    if end:
        print(result)
    else:
        print('SYJKGW')
        # 주어진 형식에 맞게 출력해줍니다.