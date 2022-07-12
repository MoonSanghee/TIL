# 6079 : [기초-종합] 언제까지 더해야 할까?

# Q. 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

# A.
# a = int(input())
# b = 0
# for i in range(a):
#     b = b + i
#     if b >= a:
#         print(i)
#         break
# A2.
# a = 0 
# b = 0
# c = int(input())
# while c > b:
#     a = a + 1
#     b = b + a
# print(a)
