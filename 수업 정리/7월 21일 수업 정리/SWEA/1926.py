# A1.
# n = int(input())
# for i in range(1, n + 1):
#     if i // 10 == 0:
#         if i % 3 == 0:
#             print('-', end = ' ')
#         else:
#             print(i, end = ' ')
#     elif i // 100 == 0:
#         if (i // 10) % 3 == 0 and (i % 10) % 3 == 0 and i % 10 != 0:
#             print('--', end = ' ')
#         elif (i // 10) % 3 == 0:
#             print('-', end = ' ')
#         elif (i % 10) % 3 == 0 and i % 10 != 0:
#             print('-', end = ' ')
#         else:
#             print(i, end = ' ')
#     else:
#         if (i // 100) % 3 == 0 and ((i // 10) % 10) % 3 == 0 and (i % 10) % 3 == 0 and i % 10 != 0:
#             print('---', end = ' ')
#         elif (i // 100) % 3 == 0 and  ((i // 10) % 10) % 3 == 0:
#             print('--', end = ' ')
#         elif (i // 100) % 3 == 0 and (i % 10) % 3 == 0 and i % 10 != 0:
#             print('--', end = ' ')
#         elif ((i // 10) % 10) % 3 == 0 and (i % 10) % 3 == 0 and i % 10 != 0:
#             print('--', end = ' ')
#         elif (i // 100) % 3 == 0:
#             print('-', end = ' ')
#         elif ((i // 10) % 10) % 3 == 0 and (i // 10) % 10 != 0:
#             print('-', end = ' ')
#         elif (i % 10) % 3 == 0 and i % 10 != 0:
#             print('-', end = ' ')
#         else:
#             print(i, end = ' ')

# A2.
# n = int(input())
# for i in range(1, n + 1):
#     if i < 10:
#         if str(i) in ['3', '6', '9']:
#             print('-', end = ' ')
#         else:
#             print(i, end = ' ')
#     elif i < 100:
#         a = ''
#         if str(i)[0] in ['3', '6', '9']:
#             a += '-'
#         if str(i)[1] in ['3', '6', '9']:
#             a += '-'
#         if a == '':
#             print(i, end = ' ')
#         else:
#             print(a, end = ' ')
#     else:
#         a = ''
#         if str(i)[0] in ['3', '6', '9']:
#             a += '-'
#         if str(i)[1] in ['3', '6', '9']:
#             a += '-'
#         if str(i)[2] in ['3', '6', '9']:
#             a += '-'
#         if a == '':
#             print(i, end = ' ')
#         else:
#             print(a, end = ' ')        

# n = int(input())
# n은 입력값

# 1부터 n까지 확인하고 값을 출력하는데 두자리 이상의 수의 경우 앞자리 수부터 확인하고
# 3, 6, 9가 들어가는지 들어가면 몇개가 들어가는지 확인 후 값을 출력 
# 각 자리에 3, 6, 9가 없으면 그 값을 그대로 출력


# 런타임 에러
# for i in range(1, n + 1):
#     a = ''
#     if (i // 100) % 3 == 0 and i // 100 != 0:
#         a += '-'
#     if ((i // 10) % 10) % 3 == 0 and (i // 10) % 10 != 0:
#         a += '-'
#     if (i % 10) % 3 == 0 and i % 10 != 0:
#         a += '-'
#     if a == '':
#         print(i, end = ' ')
#     else:
#         print(a, end = ' ')

# A3. 런타임 에러 해결
n = int(input())
for i in range(1, n + 1):
    a = ''
    for j in range(len(str(i))):
        if str(i)[j] in ['3', '6', '9']:
            a += '-'
    if a == '':
        print(i, end = ' ')
    else:
        print(a, end = ' ')