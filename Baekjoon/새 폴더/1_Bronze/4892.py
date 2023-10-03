cnt = 1
while True:
    n0 = int(input())
    # 수를 입력받아줍니다.
    if n0 == 0:
        break
    # 0이라면 확인을 멈추어줍니다.
    n1 = 3*n0
    # n1은 n0에 3을 곱한 값입니다.
    if n1 % 2:
        n2 = (n1 + 1) // 2
    else:
        n2 = n1 // 2
    # n1 값이 홀수인지 확인하고 n2를 구해줍니다.
    n3 = 3*n2
    # n3를 구해줍니다.
    n4 = n3//9
    # n4를 구해줍니다.
    if n0 == 2*n4:
        print(f"{cnt}. even {n4}")
    else:
        print(f"{cnt}. odd {n4}")
    # 최초 입력값에 따라 홀수인지 짝수인지와 n4 값을 출력해줍니다.
    cnt += 1