q = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for _ in range(q):
    a, b = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    if a < b:
        inner = b - a
        outer = 43 - (b - a)
    else:
        inner = 43 - (a - b)
        outer = a - b
    # 내선과 외선이 각 얼마나 걸리는지 구해줍니다
    if inner < outer:
        print("Inner circle line")
    elif inner > outer:
        print("Outer circle line")
    else:
        print("Same")
    # 빠른 노선을 출력해줍니다