photo = [input() for _ in range(5)]
result = ['' for _ in range(5)]
# 주어지는 사진과 결과를 담을 리스트를 만들어줍니다
for i in range(len(photo[0])):
    line = ''
    for j in range(5):
        line += photo[j][i]
    # 각 줄을 확인하여 상태를 확인하여줍니다
    if line == '.omln':
        result[0] += 'o'
        result[1] += 'w'
        result[2] += 'l'
        result[3] += 'n'
        result[4] += '.'
    elif line == 'owln.':
        result[0] += '.'
        result[1] += 'o'
        result[2] += 'm'
        result[3] += 'l'
        result[4] += 'n'
    else:
        result[0] += '.'
        result[1] += '.'
        result[2] += 'o'
        result[3] += 'L'
        result[4] += 'n'
    # 상태에 따라 변환될 형태를 담아줍니다
for line in result:
    print(line)
# 결과를 출력해줍니다