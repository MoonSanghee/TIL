# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)

# Q. 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# A.
# a, b, c = map(int, input().split())
# if (a < b) and (a < c):
#     print(a)
# elif (b < a) and (b < c):
#     print(b)
# else:
#     print(c)