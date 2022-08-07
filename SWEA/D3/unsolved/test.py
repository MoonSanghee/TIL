# seet = []
# cnt = 1
# for _ in range(10):
#     line = list(input())
#     seet.append(line)

# for i in range(10):
#     for j in range(10):
#         word = []
#         for k in range(10):
#             if j + k < 10:
#                 word += seet[i][k + j]
#         if word == word[::-1]:
#             cnt = len(word)
#             break
#         if len(word) == cnt:
#             break
#     print(i, '-----------------------------------------------', cnt)
# for i in range(10):
#     for j in range(10):
#         word = []
#         for k in range(10):
#             if j + k < 10:
#                 word += seet[j + k][i]
#         print(word, word[::-1])
#         if word == word[::-1]:
#             cnt = len(word)
#             break
#         if len(word) == cnt:
#             break
#     print(i, '--------------------------------------------', cnt)
# print(cnt)
