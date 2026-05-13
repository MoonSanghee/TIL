tc = int(input())
# 테스트케이스가 몇개 주어지는지 받아줍니다
for _ in range(tc):
    X, Y = map(int, input().split())
    # 주어지는 두 값을 받아줍니다
    print((X + Y) // 2, (X - Y) // 2)
    # 결과를 출력해줍니다