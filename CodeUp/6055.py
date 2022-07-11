# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)

# Q. 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# A.
# a, b = map(int, input().split())
# a = bool(a)
# b = bool(b)
# if (a == True) or (b == True):
#     print(True)
# else:
#     print(False)