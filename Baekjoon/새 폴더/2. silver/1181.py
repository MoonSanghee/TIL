# n = int(input())

# words = []
# length = []
# for i in range(n):
#     word = input()
#     words.append(word)
#     length.append(len(word))
# words = list(set(words))
# words = sorted(words)
# length = list(set(length))
# length = sorted(length)
# for i in length:
#     for j in words:
#         if len(j) ==i:
#             print(j)


# 찾아본 코드
# import sys

# n = int(sys.stdin.readline())
# lst = []

# for i in range(n):
#     lst.append(sys.stdin.readline().strip())
# set_lst = set(lst)
# lst = list(set_lst)
# lst.sort()
# lst.sort(key = len)
# # 키값을 이용해 길이를 기준으로도 정렬이 가능하다. 

# for i in lst:
#     print(i)

# 찾아본 코드 2 람다함수 사용
# words_num = int(input())
# words_list = []

# for _ in range(words_num):
#     word = str(input())
#     word_count = len(word)
#     words_list.append((word, word_count))

# #중복 삭제
# words_list = list(set(words_list))

# #단어 숫자 정렬 > 단어 알파벳 정렬
# words_list.sort(key = lambda word: (word[1], word[0]))

# for word in words_list:
#     print(word[0])