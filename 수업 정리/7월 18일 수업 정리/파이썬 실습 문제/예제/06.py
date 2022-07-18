# Q. 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

#  Output
#  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\

# A.
# answer가 튜플을 정의하는 ()로 정의되어있어 append를 사용할 수 없다.
# 비어있는 리스트를 정의하는 []로 바꾸어주면 값을 출력할 수 있다.
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)