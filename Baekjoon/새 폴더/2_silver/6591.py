while True:
    n, k = map(int, input().split())
    if n == k and n == 0:
        break
    # 두 수를 받고 둘 다 0일때까지 반복해줍니다
    if k == 0:
        print(1)
    # k가 0이면 1을 출력해줍니다
    else:
        n_k = n - k
        result = 1
        for i in range(n,max(k,n_k),-1) :
            result *= i
        for i in range(1,min(n_k,k) + 1) :
            result //=i
        print(result)
    # n!에서 k!*(n - k)!을 나눈값을 출력해줍니다