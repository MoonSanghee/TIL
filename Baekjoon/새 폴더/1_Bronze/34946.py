A, B, C, D = map(int, input().split())
A = A + B
# 주어지는 변수들을 받고 버스를 탈 경우 이동시간과 대기시간을 더해줍니다 
if A > D and C > D:
    print('T.T')
elif C <= D and A <= D:
    print('~.~')
elif C <= D:
    print('Walk')
else:
    print('Shuttle')
# 주어진 조건에 따라 결과를 출력해줍니다