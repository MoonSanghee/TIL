while True:
    li = list(map(int, input().split()))
    if li[0] == 0 and len(li) == 1:
        break
    
    b, p, m = li[0], li[1], li[2]

    n = int(str(p), b) % int(str(m), b)
    result = []
    
    while n >= b:
        result.append(str(n % b))
        n = n // b
    
    result.append(str(n))

    print(int(''.join(result[::-1])))