base = 'DEFGHIJKLMNOPQRSTUVWXYZABC'
new = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 카이사르 암호로 변경 후와 전의 문자열을 받아줍니다.
d = dict()
for i in range(len(base)):
    d[base[i]] = i
    # 딕셔너리에 카이사르 암호로 인덱스 값을 받아줍니다
word = input()
# 단어를 입력받아줍니다.
result = ''
# 결과를 저장할 빈 문자열을 만들어줍니다.
for i in word:
    result += new[d[i]]
    # 단어를 순회하며 카이사르 암호 적용 전의 문자로 변경시켜줍니다.
print(result)
# 결과 문자를 받아줍니다.