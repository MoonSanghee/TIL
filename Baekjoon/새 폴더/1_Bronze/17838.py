t = int(input())
# 주어지는 테스트케이스가 몇개인지 받아줍니다
for tc in range(t):
    n = input()
    # 커맨드를 받아줍니다
    if len(n) == 7 and (n[0] == n[1] == n[4]) and (n[2] == n[3] == n[5] == n[6]) and n[0] != n[2]:
        print(1)
    else:
        print(0)
    # 유효한 커맨드인지 확인하여 결과를 출력해줍니다