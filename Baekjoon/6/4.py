# 6-4 문제번호 2675

# Q. 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# A.
S = int(input())
for i in range(S) :
    R, P = input().split()
    for i in P:
        (print(i*int(R), end = ""))
    print() # 두번째 for 문에 끝나고 줄 바꾸지 않고 이어서 쓰도록 표현해 두었기에
            # 반복이 끝나고 줄을 바꾸도록 반복문 밖에 print()를 추가해준다.