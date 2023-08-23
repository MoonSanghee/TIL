n = int(input())
# 테스트 케이스의 수를 받아줍니다.
for _ in range(n):
    c, v = map(int, input().split())
    # 캔디와 형제의 수를 받아줍니다.
    candy = c // v
    dad = c % v
    # 내가 받을 캔디의 수와 아버지의 캔디 수를 구해줍니다.
    print(f'You get {candy} piece(s) and your dad gets {dad} piece(s).')
    # 형식에 맞게 출력하여줍니다.