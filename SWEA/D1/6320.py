player1 = input()
player2 = input()

li = []
p1 = input()
p2 = input()
li.append(p1)
li.append(p2)

if '가위' in li:
    if '바위' in li:
        print('바위가 이겼습니다!')
    else:
        print('가위가 이겼습니다!')
else:
    print('보가 이겼습니다!')