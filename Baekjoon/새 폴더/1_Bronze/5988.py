n = int(input())
# n번 수를 입력 받습니다.
for _ in range(n):
    if int(input()) % 2:
        print('odd')
        # 짝수면 odd
    else:
        print('even')
        # 홀수면 even을 출력해줍니다.