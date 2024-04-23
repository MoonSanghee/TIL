yeongil = input()
result = ''

if yeongil[0] == 'E':
    result += 'I'
else:
    result += 'E'

if yeongil[1] == 'S':
    result += 'N'
else:
    result += 'S'

if yeongil[2] == 'T':
    result += 'F'
else:
    result += 'T'

if yeongil[3] == 'J':
    result += 'P'
else:
    result += 'J'

print(result)
# 연길이의 MBTI를 받고 반대의 값을 담아 출력해줍니다.