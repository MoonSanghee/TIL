# 문제 14. 문자의 갯수 구하기

# Q. 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지

# A.
# word = input()
# 개수 = 0
# for i in word:
#     if i == 'a':
#         개수 +=1
# print(개수)


# 문제 15. 문자의 위치 구하기

# Q. 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

# A.
# word = input()
# 자리수 = 0
# 없음 = 0
# for i in word:
#     자리수 += 1
#     if i == 'a':
#         print(자리수)
#         break
# for i in word:
#     없음 += 1
# if 자리수 == 없음:
#     print(-1)

# 문제 15-2

# Q. 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지

# A.
# word = input()
# 자리수 = 0
# for i in word:
#     자리수 += 1
#     if i == 'a':
#         print(자리수, end = ' ') # 한줄에 각 값을 띄워서 표시


# 문제 16. 모음 등장 여부 확인하기

# Q. 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

# A.
# word = input()
# vowel = 0
# for i in word:
#     if i =='a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
#         vowel += 1
# print(vowel)


# 문제 17. 소문자-대문자 변환하기 

# Q. 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

# A.
# word = input()
# new_word =''
# for i in word:
#     if ord(i) > 95:
#         i = chr(ord(i) - 32)
#         new_word += i
#     else:
#         i = chr(ord(i) + 32)
#         new_word += i
# print(new_word)


# 문제 18.  알파벳 등장 갯수 구하기

# Q. 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

# A.
# word = input()
# 글자 = []
# 쓴것 = []
# dic = {}
# for i in word:
#     글자 += i
# for i in 글자:
#     if i not in 쓴것:
#         print(i, 글자.count(i))
#         쓴것 += i

# 풀이 설명
# # A1.
# word = 'banana'

# result = {}
# for char in word:
#     #딕셔너리에 키가 없으면?
#     if not char in result.keys():
#         # 키랑 값을 0으로 초기화한다.
#         result[char] = 1
#     else:
#         result[char] = result[char] + 1
# print(result)

# # A2.
# result = {}
# for char in word:
#     result[char] = result.get(char, 0) + 1
# print(result)

# for key in result:
#     print(key, result[key])