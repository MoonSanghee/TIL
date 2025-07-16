n = int(input())
word = input()
# 아이디의 길이와 아이디를 받아줍니다
result = ''
# 변환한 아이디를 담을 변수를 설정해줍니다
for i in word:
    if i == 'I':
        result += 'i'
    elif i == 'l':
        result += 'L'
# 입력값을 변환하여 result에 담아줍니다
print(result)
# 결과를 출력해줍니다