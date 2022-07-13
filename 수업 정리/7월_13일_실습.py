# 문제 09. 득표수 구하기

# Q. 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
# students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# # A.
# a = 0
# for i in students:
#     if i == '이영희':
#         a += 1
# print(a)

# 문제 10. 5의 개수 구하기

# Q. 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

# A.
# five = 0
# 리스트 = list(map(int, input().split(',')))
# for i in 리스트:
#     if i == 5:
#         five += 1
# print(five)

# 문제 11. 구구단 출력하기

# Q. 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

# A.
# for i in range(2, 10):
#     print(f'{i}단')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j}')

# 문제 12. 문자열 조작하기

# Q. 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

# A.
# word = input()
# re_word = ''
# for i in word:
#     if i != 'a':
#         re_word += i
# print(re_word)

# 문제 13. 문자열 조작하기

# Q. 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

# A.
# word = input()
# re_word = word[::-1]
# print(re_word)

# 예제 01. 기초함수

# Q. 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오

# A.
# n = int(input())
# def cube(n):
#     return n**3
# print(cube(n))

# 예제 02 기초 함수

# Q. 가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
# 사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

# * 사각형 넓이 : 가로 * 세로 
# * 사각형 둘레 : (가로 + 세로) * 2

# A. 
# a, b = map(int, input().split())
# def rectangle(a, b):
#     return a * b, (a + b) * 2
# print(f'''사각형 넓이 : {rectangle(a, b)[0]}
# 사각형 둘레 : {rectangle(a, b)[1]}''')