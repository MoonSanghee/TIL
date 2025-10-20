base = input()
names = list(base.split())
# 주어지는 입력을 받아 원본을 문자열형태 띄워쓰기를 나누어 리스트에 담은 형태로 받아줍니다
if '(' not in base:
    print(*names)
    print('-')
    # 괄호가 없다면 부역명이 없습니다
else:
    main = []
    cnt = 0
    # 부역명이 있다면 역명을 모아담고
    while True:
        if '(' in names[cnt]:
            others = names[cnt:]
            break
        else:
            main.append(names[cnt])
            cnt += 1
    
    others[0] = others[0][1:]
    others[-1] = others[-1][:-1]
    # 부역명의 열림, 닫힘 기호를 없애줍니다
    print(*main)
    print(*others)
    # 결과를 출력해줍니다