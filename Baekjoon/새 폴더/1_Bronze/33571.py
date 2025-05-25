one = 'AabDdegOoPpQqR@'
# 구멍이 하나가 있는 문자들을 모아줍니다
# 두 개가 있는것은 대문자 B 하나뿐이므로 따로 모으지 않습니다
sentence = input()
# 주어지는 문장을 받아줍니다
result = 0
# 구멍의 개수를 담을 변수를 설정해줍니다
for i in sentence:
    if i == 'B':
        result += 2
    elif i in one:
        result += 1
# 모든 문자를 확인하며 구멍의 개수를 확인해줍니다
print(result)
# 결과를 출력해줍니다