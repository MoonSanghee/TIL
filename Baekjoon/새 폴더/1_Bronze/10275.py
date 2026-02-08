t = int(input())
# 주어지는 테스트케이스의 수를 받아줍니다
for _ in range(t):
    n, a, b = map(int, input().split())
    small = bin(min(a, b))[::-1]
    # 주어지는 변수들을 받아 두 가방중 작은쪽을 이진수로 변환하고 뒤집어줍니다
    for i in range(len(small)):
        if small[i] == '1':
            cnt = i
            break
    # 필요한 최소 단위를 확인해줍니다
    print(n - cnt)
    # 결과를 출력해줍니다