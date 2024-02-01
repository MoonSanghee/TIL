while True:
    li = list(map(int, input().split()))
    if li[0] == 0 and len(li) == 1:
        break
    # 수를 받아줍니다.
    b, p, m = li[0], li[1], li[2]
    # b, p, m을 구해줍니다.
    n = int(str(p), b) % int(str(m), b)
    # b진수 p,m을 10진수로 변환시켜 나눈값을 구해줍니다.
    result = []
    
    while n >= b:
        result.append(str(n % b))
        n = n // b
        # 나머지 n을 b진법으로 변환해줍니다.
    
    result.append(str(n))
    print(int(''.join(result[::-1])))
    # b진법으로 바꾼 결과를 출력해줍니다.