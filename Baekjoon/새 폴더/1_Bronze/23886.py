x = input()
flag = True
# 주어지는 수를 받고 알프수가 성립하는지를 담을 변수를 설정해줍니다
if int(x[1]) < int(x[0]) or int(x[-1]) > int(x[-2]):
    flag = False
    # 시작과 마지막 기울기가 알프수가 성립하는지 확인하여줍니다
else:
    for i in range(1, len(x) - 1):
        if int(x[i]) == int(x[i - 1]) or int(x[i]) == int(x[i + 1]):
            flag = False
            break
        # 평지가 있다면 성립하지 않습니다
        elif (int(x[i]) - int(x[i - 1])) * (int(x[i + 1]) - int(x[i])) > 0:
            if (int(x[i]) - int(x[i - 1])) != (int(x[i + 1]) - int(x[i])):
                flag = False
                break
        # 기울기의 방향이 같을때 기울기가 다르다면 성립하지 않습니다

if flag:
    print("ALPSOO")
else:
    print("NON ALPSOO")
# 결과를 출력해줍니다