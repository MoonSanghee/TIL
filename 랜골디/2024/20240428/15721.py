people = int(input())
target = int(input())
find = int(input())
# 게임에 참여하는 사람의 수와 구하고자하는 구호의 차례 찾으려는 구호를 받아줍니다.
fun, daegi = 0, 0
cycle = 1
turn = 0
# 뻔과 데기가 몇번씩 나왔는지 확인할 변수와 몇 바퀴째 돌고있고 어떤 구호를 외칠 차례인지 받아줍니다.
# 뻔 / 데기 / 뻔 / 데기 / 뻔  * (cycle + 1) / 데기 * (cycle + 1)
# 1번의 사이클은 위의 6단계로 나뉘어집니다. 
while True:
    if find == 1:
        if daegi >= target:
            break
    else:
        if fun >= target:
            break
    # 목표로 하는만큼 구호가 나왔다면 확인을 멈추어줍니다.
    if turn == 0:
        fun += 1
    elif turn == 1:
        daegi += 1
    elif turn == 2:
        fun += 1
    elif turn == 3:
        daegi += 1
    elif turn == 4:
        for _ in range(cycle + 1):
            fun += 1
            if find == 0:
                if target == fun:
                    break
    else:
        for _ in range(cycle + 1):
            daegi += 1
            if find == 1:
                if target == daegi:
                    break
        cycle += 1
    # 각 차례에 맞는 동작을 실행해줍니다.
    # 마지막 차레를 마쳤다면 다음 사이클로 넘겨줍니다.
    turn += 1
    turn %= 6
    # 차례를 진행시켜줍니다.

result = (fun + daegi) % people
if result:
    print(result - 1)
else:
    print(people - 1)
# 0번자리부터 시작되므로 뻔과 데기를 합하여 전체 구호가 외쳐진 수를 사람 수로 
# 나눈 나머지가 존재한다면 나머지에 1을 뺀 값을 없다면 사람중에 마지막 번호를 출력해줍니다.