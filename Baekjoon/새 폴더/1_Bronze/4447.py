n = int(input())
# 주어지는 문자의 수를 받아줍니다
for _ in range(n):
    g, b = 0, 0
    command = input()
    for i in command:
        if i.lower() == 'b':
            b += 1
        elif i.lower() == 'g':
            g += 1
    # 문장에서 g와 b의 수를 확인해줍니다
    if g > b:
        print(f'{command} is GOOD')
    elif g == b:
        print(f'{command} is NEUTRAL')
    else:
        print(f'{command} is A BADDY')
    # 결과를 주어진 형식에 맞춰 출력해줍니다