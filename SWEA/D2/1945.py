import sys

sys.stdin = open("1945_input.txt", "r")

a = int(input())
for i in range(a):
    b = int(input())
    ac = 0
    bc = 0
    cc = 0
    dc = 0
    ec = 0
    for j in range(2, b):
        if (b % 2) == 0 and (j % 2) == 0:
            ac += 1
            b //= 2
            j = 2
        elif (b % 3) == 0 and (j % 3) == 0:
            bc += 1
            b //= 3
            j = 2
        elif (b % 5) == 0 and (j % 5) == 0:
            cc += 1
            b //= 5
            j = 2
        elif (b % 7) == 0 and (j % 7) == 0:
            dc += 1
            b //= 7
            j = 2
        elif (b % 11) == 0 and (j % 11) == 0:
            ec += 1
            b //= 11
            j = 2
    print(f'#{i + 1}', ac, bc, cc, dc, ec, end = ' ')
    print()


# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     num_lst = [2,3,5,7,11]
#     cnt_lst = [0,0,0,0,0]
#     for i in range(5):
#         while N % num_lst[i] == 0:
#             cnt_lst[i] += 1
#             N //= num_lst[i]
#     print(f'#{tc} ', end='')
#     print(*cnt_lst)
# 2,3,5,7,11을 가지는 리스트와 각 0,0,0,0,0을 가지는 리스트를 이용해 
# 반복문을 활용하면 더 간편한 식을 만들수 있다.