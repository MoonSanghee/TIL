# Q. 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# words = list(map(int, input().split()))
# print(words)

# Input
# I'm Tuotur 6

# Output
# ["I'm", 'Tutor', '6']

# A.
# words는 입력값을 정수형으로 변환시켜 나누게 되어있는데 입력값이 정수형이 아니라 에러가 나옴
# 그래서 int가 아닌 str형으로 받도록 변경하여줍니다.
# words = list(map(str, input().split()))
# print(words)