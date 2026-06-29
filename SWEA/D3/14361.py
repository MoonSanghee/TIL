T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = input()
    d = dict()
    for i in n:
        d[i] = d.get(i, 0) + 1
    # 주어지는 수를 받아 각 자리수들을 이루는 수의 개수를 확인해줍니다
    for i in range(2, 10):
        num = str(int(n) * i)
        # 재배열하여 자릿수가 바뀔수는 없으므로 2~9배까지를 확인해줍니다
        if len(num) != len(n):
            continue
        # i를 곱한 값의 자릿값이 바뀐다면 확인을 건너뜁니다
        else:
            check = dict()
            for j in num:
                check[j] = check.get(j, 0) + 1
            if check == d:
                print(f'#{t + 1} possible')
                break
            # i를 곱한값을 재배열하여 만들수 있는지 확인해줍니다
    else:
        print(f'#{t + 1} impossible')
        # 결과를 주어진 양식에 맞춰 출력해줍니다