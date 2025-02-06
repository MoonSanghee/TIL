p, w = map(int, input().split())
massage = input()
# 버튼을 누르는데 걸리는 시간과 같은 버튼의 문자를 연속해 입력하기위해 기다려야하는 시간을 받고 메시지를 받아줍니다
d = {
    1 : [' '],
    2 : ['A', 'B', 'C'], 
    3 : ['D', 'E', 'F'],
    4 : ['G', 'H', 'I'], 
    5 : ['J', 'K', 'L'], 
    6 : ['M', 'N', 'O'],
    7 : ['P', 'Q', 'R', 'S'], 
    8 : ['T', 'U', 'V'], 
    9 : ['W', 'X', 'Y', 'Z']}
# 각 자판에 문자를 담아줍니다
check = 0
result = 0
# 연속한 자판에 위치한 문자인지 확인하기위한 변수와 결과를 담을 변수를 설정해줍니다
for i in massage:
    for j in d:
        if i in d[j]:
            cnt = d[j].index(i) + 1
            if check == j and check != 1:
                result += w
            check = j
            result += p * cnt
            # 연속하고 띄워쓰는 경우가 아니라면 w만큼을 더해주고 버튼을 누르는 시간을 더해줍니다
print(result)
# 결과를 출력해줍니다