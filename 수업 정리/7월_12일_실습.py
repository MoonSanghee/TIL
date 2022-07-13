# 문제 01. 수 구분하기

# Q.주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.

# A.
# a = int(input())
# if a % 3 = 0 and a % 2 = 0
# 	print('참')
# else
# 	print('거짓')


# 문제 02. 길이 구하기

# Q. 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len() 함수 사용 금지

# A.
# a = input()
# b = 0
# for i in a
#     b += 1
# print(b)


# 문제 03. 합 구하기

# Q. 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# A.
# 1)
# a = int(input())
# b = 0
# c = 0
# while b != a:
#     b += 1
#     c += b
# print(c)

# 2)
# a = int(input())
# b = 0
# c = 0
# for i in range(a+1):
#     c = b + c
#     b += 1
# print(c)


# 문제 04. 곱 구하기

# Q. 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# A.
# 1)
# a = int(input())
# b = 1
# c = 1
# while b != a:
#     b += 1
#     c =  b
# print(c)

# 2)
# a = int(input())
# c = 1
# for i in range(1, a+1):
#     c = i
# print(c)


# 문제 05. 평균 구하기

# Q. 1부터 n까지의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

# A.
# x = input().split()
# b = 0
# c = 0
# for i in x:
#     b += 1
#     c += b
# print(c/b)  # 소숫점 이하 포함
# print(c//b) # 몫만


# 문제 06. 최댓값 구하기

# Q. 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# A.
# x = list(map(int, input().split(', ')))
# b = x[0]
# for i in x:
#     if i > b:
#         b = i
# print(b)


# 문제 07. 최솟값 구하기

# Q. 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

# A.
# x = list(map(int, input().split(', ')))
# b = x[0]
# for i in x:
#     if i < b:
#         b = i
# print(b)


# 문제 08. 두번째로 큰 수 구하기

# Q. 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# A.
# x = list(map(int, input().split(', ')))
# b = x[0]
# c = x[0]
# for i in x:
#     if i > b:
#         c = b
#         b = i
#     elif c < i and i < b:
#         # c < i < b로 표현 가능
#         c = i
# print(c)