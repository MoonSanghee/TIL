n = input()

zero = False
one = False
two = False
eight = False
# 주어지는 수를 받고 출력해야하는 형태를 담을 변수를 설정해줍니다.
d = {'2' : 0, '0' : 0, '1' : 0, '8' : 0}
# 2,0,1,8을 담을 딕셔너리를 만들어줍니다.
for i in n:
    if i not in d:
        zero = True
    else:
        d[i] += 1
# 2,0,1,8이외의 수가 들어온다면 zero를 출력해주기위해 zero를 True로 바꾸어주고 아니면 각 수의 값을 갱신해줍니다.
if zero == False:
    for i in d:
        if d[i] == 0:
            one = True
            break
    else:
        if d['0'] == d['2'] and d['0'] == d['8'] and d['0'] == d['1']:
            eight = True
        else:
            two = True
# 출력할 값이 0이 아니라면 조건을 확인하여 출력해야하는 값을 찾아줍니다.
if zero:
    print(0)
elif one:
    print(1)
elif two:
    print(2)
elif eight:
    print(8)
# 결과를 출력해줍니다.