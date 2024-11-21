t = int(input())
# 테스트 케이스의 개수를 받아줍니다
for _ in range(t):
    n, m = input().split()
    one = 0
    zero = 0
    # 두 개의 이진수를 받아줍니다
    for i in range(len(n)):
        if n[i] != m[i]:
            if m[i] == '1':
                one += 1
            else:
                zero += 1
    # 두 수의 자리 값이 다를때 1인 쪽을 표시해줍니다
    print(max(one, zero))
    # 많이 바꾸어야하는 쪽을 출력해줍니다