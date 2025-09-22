n = int(input())
cnt = list(map(int, input().split()))
recipe = input()
flag = True
# 주어지는 변수들을 받아줍니다
if recipe[0] != recipe[-1] or recipe[0] != 'a':
    flag = False
# 가장 앞이나 마지막이 빵인지 확인해줍니다
for i in range(1, len(recipe)):
    if recipe[i] == 'a':
        cnt[0] -= 1
    elif recipe[i] == 'b':
        cnt[1] -= 1
    elif recipe[i] == 'c':
        cnt[2] -= 1
    else:
        cnt[3] -= 1
    
    if recipe[i] == recipe[i - 1]:
        flag = False
        break
    elif -1 in cnt:
        flag = False
        break
    # 연속하는 재료가 오거나 재료가 부족하다면 상태를 변경해줍니다
if flag:
    print('Yes')
else:
    print('No')
# 결과를 출력해줍니다