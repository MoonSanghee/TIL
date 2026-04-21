n = int(input())
# 주어지는 테스트케이스의 수를 받아줍니다
for _ in range(n):
    x, y = map(int, input().split())
    if x >= y:
        print("MMM BRAINS")
    else:
        print("NO BRAINS")
    # 주어지는 수를 받아 결과를 출력해줍니다