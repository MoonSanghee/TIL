# SWEA 1234

# 나의 풀이
# for test in range(1, 11):
#     length, word = map(str, input().split())
#     word = list(word)
#     done = 0
#     while done == 0:
#         for i in range(len(word) - 1):
#             if word[i] == word[i + 1]:
#                 word = word[:i:] + word[i + 2::]
#                 break
#         else:
#             done = 1
#     password = ''
#     for i in word:
#         password += str(i)
#     print(f'#{test} {password}')

# 리뷰한 풀이
for test in range(1, 11):
    l, w = input().split()
    check = list(w)
    stack = []
    for i in range(len(w)):
        if stack:
            if stack[-1] == check[i]:
                stack.pop()
            else:
                stack.append(check[i])
        else:
            stack.append(check[i])
    result = ''.join(stack)
    print(f'#{test} {result}')
