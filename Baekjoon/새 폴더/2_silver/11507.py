keyword = input()
# 주어지는 입력을 받아줍니다
flag = True
# 중복되는 카드가 있는지 확인할 변수를 만들어줍니다
d = dict()
for i in 'PKHT':
    d[i] = []
# 카드의 문양별로 가진 카드를 담을 변수를 만들어줍니다
for i in range(0, len(keyword), 3):
    if keyword[i + 1: i + 3] in d[keyword[i]]:
        flag = False
    d[keyword[i]].append(keyword[i+ 1: i + 3])
# 각 카드값을 확인해서 중복인지 확인하고 가진 카드를 넣어줍니다
if flag:
    for i in 'PKHT':
        print(13 - len(d[i]), end = ' ')
else:
    print('GRESKA')
    # 중복된 카드가 있는지 확인하여 주어진 형식에 맞게 출력해줍니다