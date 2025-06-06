number, name = input().split()
# 주어지는 표기법과 변수명을 받아줍니다
if number == '2':
    words = name.split('_')
else:
    words = []
    word = ''
    for i in name:
        if i.isupper():
            words.append(word)
            word = i
        else:
            word += i
    words.append(word)
    if number == '3':
        words = words[1:]
# 표기법에 따라 주어지는 단어들을 나누어 리스트에 담아줍니다
camel = words[0].lower()
snake = words[0].lower()
# 카멜 표기법과 스네이크 표기법은 시작 단어가 소문자로 시작하므로 첫 단어를 소문자로 받아줍니다
for i in range(1, len(words)):
    camel += words[i][0].upper() + words[i][1:]
    snake += '_' + words[i].lower()
# 각 표기법에 맞게 뒤의 단어들을 이어줍니다
pascal = camel[0].upper() + camel[1:]
# 카멜 표기법의 가장 앞자리를 바꾸어 파스칼 표기법을 구해줍니다
print(camel)
print(snake)
print(pascal)
# 각 표기법을 사용한 경우를 차례대로 출력해줍니다