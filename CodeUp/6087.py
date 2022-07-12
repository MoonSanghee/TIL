# 6087 : [기초-종합] 3의 배수는 통과(설명)

# Q. 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.

# A1.
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 != 0:
#         continue
#     print(i, end= ' ')
# A2.
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 != 0:
#         print(i, end= ' ')