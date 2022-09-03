sen = input()
result = []
cnt = 0
for i in sen:
    if i == 'X':
        cnt += 1
    else:
        if (cnt % 2) == 1:
            result = [-1]
            break
        else:
            word = ''
            word += (cnt//4) * 'AAAA'
            cnt %= 4
            word += (cnt//2) * 'BB'
            cnt = 0
            result.append(word)
        result.append('.')
else:
    if (cnt % 2) == 1:
        result = [-1]
    else:
        word = ''
        word += (cnt//4) * 'AAAA'
        cnt %= 4
        word += (cnt//2) * 'BB'
        cnt = 0
        result.append(word)
for i in result:
    print(i, end='')
print()

# replace 메서드를 이용하면 문자열을 수정할 수 있다!!
sen = input()
sen = sen.replace('XXXX', 'AAAA')
sen = sen.replace('XX', 'BB')

if 'X' in sen:
    print(-1)
else:
    print(sen)