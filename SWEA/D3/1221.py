num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
test_case = int(input())

for test in range(1, test_case + 1):
    test_num = input().split()
    print(test_num[0])
    
    numbers = list(map(str, input().split()))
    cnt = dict()
    for i in numbers:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for i in num:
        for j in range(cnt[i]):
            if i in cnt and cnt[i] > 0:
                print(i, end = ' ')
                cnt[i] -= 1
    print()
# num = {
#     "ZRO"   : 0,
#     "ONE"   : 1,
#     "TWO"   : 2,
#     "THR"   : 3,
#     "FOR"   : 4,
#     "FIV"   : 5,
#     "SIX"   : 6,
#     "SVN"   : 7,
#     "EGT"   : 8,
#     "NIN"   : 9
# }