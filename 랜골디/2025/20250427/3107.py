adress = list(input().split(':'))
# IPv6 주소를 받아줍니다
if adress[0] == '':
    adress = adress[1:]
elif adress[-1] == '':
    adress = adress[: -1]
# 주소의 시작이나 마지막이 생략의 범위에 포함된다면 공백이 2개가 리스트에 포함되므로 하나씩을 지워줍니다
result = ''
for i in range(len(adress)):
    if adress[i] == '':result += '0000:' * (8 - len(adress))
    else:result += adress[i].zfill(4) + ':'
# 주소를 순회하며 생략된 부분이라면 자릿수에 맞게 0000을 추가해주고 아니라면 주소를 4자리로 맞추어 넣어줍니다
print(result[:-1])
# 모든 값의 뒤에 :을 추가하였으므로 결과의 마지막 자릿값을 제외한 결과를 출력해줍니다