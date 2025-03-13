import sys
input = sys.stdin.readline
s,n,m = map(int,input().split())
cnt = 0
# 주어지는 가변 배열의 초기 크기와 입력 삭제 명령의 횟수를 받고 사용중인 크기를 담을 변수를 설정해줍니다
for _ in range(n+m):
    signal = int(input())
    if signal == 1:
        if s == cnt:
            s += s
        cnt += 1
    else:
        cnt -= 1
    # 입력 신호를 받아 사용해야하는 크기가 현재 크기보다 크다면 2배씩 크게 만들어줍니다
print(s)
# 결과를 출력해줍니다