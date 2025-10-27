n = int(input())
hangers = list(map(int, input().split()))
shirts, pants = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
for i in hangers:
    if i == 1:
        shirts -= 1
    elif i == 2:
        pants -= 1
# 상의 또는 하의 전용 옷걸이의 개수를 옷과 매칭해줍니다
result = []

if 0 > shirts or 0 > pants:
    print("NO")
    # 상의나 하의가 모자라다면 NO를 출력해줍니다
else:
    for i in hangers:
        if i == 1:
            result.append('U')
        elif i == 2:
            result.append('D')
        else:
            if shirts:
                shirts -= 1
                result.append('U')
            else:
                result.append('D')
    print("YES")
    print(''.join(result))
    # 행거를 확인하며 걸 수 있는 옷을 리스트에 담아 결과를 출력해줍니다