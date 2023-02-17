def solution(numbers, hand):
    answer = ''
    pad = {1 : [0, 0], 
           2 : [0, 1], 
           3 : [0, 2], 
           4 : [1, 0], 
           5 : [1, 1], 
           6 : [1, 2], 
           7 : [2, 0], 
           8 : [2, 1], 
           9 : [2, 2], 
           0 : [3, 1], 
           '*' : [3, 0], 
           '#' : [3, 2]}
    # 각 자판의 좌표를 딕셔너리 형태로 맞추어줍니다.
    lf = [3, 0]
    rf = [3, 2]
    # 왼손가락과 오른손가락의 위치를 지정해줍니다.
    for num in numbers:
        if num in [1, 4, 7]:
            lf = pad[num]
            answer += 'L'
        elif num in [3, 6, 9]:
            rf = pad[num]
            answer += 'R'
            # 누를 키가 왼쪽에 있으면 왼손으로 누르고 왼손을 이동하고
            # 오른쪽에 있으면 오른손으로 누르고 오른손을 이동시켜줍니다.
        else:
            leftdis = abs(pad[num][0] - lf[0]) + abs(pad[num][1] - lf[1])
            rightdis = abs(pad[num][0] - rf[0]) + abs(pad[num][1] - rf[1])
            # 가운데 위치한 버튼이라면 양 손에서 버튼까지의 거리를 확인해주고
            if hand == 'right':
                if leftdis >= rightdis:
                    rf = pad[num]
                    answer += 'R'
                else:
                    lf = pad[num]
                    answer += 'L'
            # 오른손잡이라면 오른손이 더 가깝거나 같을 경우 오른손으로 누르고 위치를 옮겨주고
            # 오른손이 멀 경우 왼손으로 누르고 왼손을 이동시켜줍니다.
            else:
                if leftdis > rightdis:
                    rf = pad[num]
                    answer += 'R'
                else:
                    lf = pad[num]
                    answer += 'L'
            # 왼손잡이의 경우 오른손이 더 가까이 위치했을 경우 오른손으로 버튼을 누르고 이동시켜주고
            # 그 외의 경우 왼손으로 누르고 왼손을 이동시켜줍니다.
    return answer
    # 저장된 누른 순서를 출력해줍니다.