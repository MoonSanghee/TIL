word = input()
# 주어지는 단어를 받아줍니다
if word == word[::-1]:
    print('true')
else:
    print('false')
# 팰린드롬인지 확인하여 결과를 출력해줍니다