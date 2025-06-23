command = input()
# 주어지는 식을 받아줍니다
cnt = [dict({"C" : 0, "H" : 0, "O" : 0}) for _ in range(3)]
idx = 0
# M1, M2, M3의 식에서 CHO의 개수를 각각 담을 딕셔너리를 3개 만들어 리스트에 넣어줍니다
for i in range(len(command)):
    if command[i] == "C":
        cnt[idx]["C"] +=1
    elif command[i] == "H":
        cnt[idx]["H"] += 1
    elif command[i] == "O":
        cnt[idx]["O"] += 1
    # 분자라면 각각 한 개씩을 추가해줍니다
    elif command[i] in "+=":
        idx += 1
    # 더하기나 등호라면 다음 자리로 옮겨줍니다
    else:
        cnt[idx][command[i - 1]] += int(command[i]) - 1
    # 주어지는 입력이 숫자라면 앞의 분자를 주어진 숫자 - 1개만큼 더해줍니다
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            # 계수가 한자리 수로 한정되었으므로 한 자리수를 순환해서 답을 찾을수 있습니다
            # M1, M2, M3가 차례대로 가장 작은 경우를 출력하므로 i, j, k를 M1, M2, M3의 계수에 곱해줍니다
            flag = True
            for x in "CHO":
                if cnt[0][x] * i + cnt[1][x] * j != cnt[2][x] * k:
                    flag = False
            if flag:
                print(i, j, k)
                exit()
                # 각 계수를 곱해 더한 분자의 개수가 일치되면 i, j, k값을 출력하고 3중 반복을 멈추기위해 exit을 사용해줍니다