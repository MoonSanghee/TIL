t = int(input())
# 주어지는 테스트케이스가 몇개인지 확인해줍니다.
for _ in range(t):
    line = input()
    # 암호문을 받아줍니다. 
    d = dict()
    # 각 문자가 몇개인지 담을 딕셔너리를 만들고 띄워쓰기가 아니면 문자의 개수를 딕셔너리에 담아줍니다.
    for i in line:
        if i != ' ':
            d[i] = d.get(i, 0) + 1
    
    letter = ''
    cnt = 0

    for i in d:
        if d[i] > cnt:
            letter = i
            cnt = d[i]
        elif d[i] == cnt:
            letter = '?'
    print(letter)
    # 딕셔너리를 확인하여 가장 많이 나오는 문자가 하나라면 문자를 아니면 물음표를 출력해줍니다.