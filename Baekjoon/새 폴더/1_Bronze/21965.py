n = int(input())
arr = list(map(int, input().split()))
# 수열의 길이와 수열을 받아줍니다
turn = 0
flag = True
# 높이가 몇번 변하는지 담을 변수와 산인지 확인할 변수를 정해줍니다
for i in range(1, n):
    if arr[i - 1] == arr[i]:
        flag = False
        break
    # 연속하는 수가 같다면 산이 아닙니다
    else:
        if turn == 0:
            if arr[i - 1] > arr[i]:
                turn += 1
            # 높이가 처음 낮아지는것을 확인해줍니다
        elif turn == 1:
            if arr[i - 1] < arr[i]:
                flag = False
                break
            # 높이가 낮아졌다가 다시 높아진다면 산이 아닙니다

if flag:
    print("YES")
else:
    print("NO")
# 결과를 출력해줍니다