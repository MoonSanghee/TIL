L, R = input().split()
cnt = 0
if len(L) != len(R):
    print(cnt)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)
    # 두 수의 길이가 다르면 8이 하나도 포함되지 않을 수 있으니 0을 출력하고
    # 길이가 같으면 가장 앞 자리부터 두 수가 같은지 확인하고 두 수가 같고 
    # 8인 경우 8을 하나 필수적으로 가지게 되어 cnt를 1 증가시켜줍니다.