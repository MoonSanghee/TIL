n = int(input())
A = list(map(int,input().split()))
battery = 2
percent = 2
# 휴대폰에 연결할 수와 연결할 휴대폰의 번호들을 받아줍니다
for i in range(n-1):
    if A[i]==A[i+1]:
        percent*=2
        battery+=percent
        if battery >= 100:
            battery = 0
            percent = 1
    else:
        battery+=2
        percent = 2
        if battery >= 100:
            battery = 0
            percent = 1
    # 연속하여 같은 휴대폰이 놓여있다면 소비 전력이 이전의 2배가 되고 아니면 2만큼 소비됩니다.
    # 배터리를 모두 사용하였다면 충전을 진행하기때문에 값을 초기화해줍니다
print(battery)
# 연결이 끝난 후에 배터리 소모량을 출력해줍니다