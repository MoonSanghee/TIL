t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    a, b = map(int, input().split())
    # 주어지는 두 수를 받아줍니다
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
        # 두 수가 같은 공통 노드를 찾을때까지 큰 수를 부모 노드로 갱신해줍니다
    print(a * 10)
    # 찾은 노드에 10을 곱한 값을 출력해줍니다