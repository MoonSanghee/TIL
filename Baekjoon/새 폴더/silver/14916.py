n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    cnt = 0
    i = 0
    while True:
        if n % 5 == 0:
            cnt += n // 5
            break
        else:
            n -= 2
            cnt += 1
        
        if n < 0:
            break
    if n < 0:
        print(-1)
    else:
        print(cnt)



# n = int(input())
# if n % 5 == 0:
#     print(n // 5)
# else:
#     five = n // 5
#     base = n % 5
#     while base < n:
#         if base % 2 == 0:
#             two = base // 2
#             break
#         base += 5
#         five -= 1
#     if base % 2 == 0:
#         print(five + two)
#     else:
#         print(-1)