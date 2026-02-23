T = int(input())
# 테스트 케이스의 개수를 받아줍니다
for _ in range(T):
    N = int(input())
    # 주어지는 정수를 받아줍니다
    if (N + 1) % (N % 100) == 0:
        print("Good")
    else:
        print("Bye")
    # 주어진 조건에 비교하여 결과를 출력해줍니다