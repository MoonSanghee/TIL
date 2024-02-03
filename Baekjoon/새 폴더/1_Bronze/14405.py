word = input()
# 단어를 받아줍니다.
while word:
    if word[:2] == 'pi' or word[:2] == 'ka':
        word = word[2:]
    elif word[:3] == 'chu':
        word = word[3:]
    else:
        break
# 주어진 세 단어로 이루어져있는지 확인해줍니다.

if word:
    print('NO')
else:
    print('YES')
# 세 단어 이외의 단어가 남았다면 NO 세 단어로만 이루어져있으면 YES를 출력합니다.