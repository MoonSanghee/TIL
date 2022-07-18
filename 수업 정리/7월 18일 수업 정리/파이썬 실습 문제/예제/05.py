# Q. 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# number = 22020718
# print(len(number))

# Output
# 8

# A.
# len()함수는 문자열의 길이를 나타내는 함수이다
# number에 입력된 값이 정수이기에 오류가 발생한다.
# print함수 안에 넣을 값을 len(str(number))로 바꾸어 문자열의 길이를 내놓도록 하면 해결할 수 있다.
# number = 22020718
# print(len(str(number)))