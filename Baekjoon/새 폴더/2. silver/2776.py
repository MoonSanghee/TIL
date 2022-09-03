test_case = int(input())

for test in range(test_case):
    follow = int(input())
    f_num = list(map(int, input().split()))
    ask = int(input())
    a_num = list(map(int, input().split()))
    for i in a_num:
        if i in f_num:
            print(1)
        else:
            print(0)