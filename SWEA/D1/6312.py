li = list(input().split())
flag = True
result = 1

for i in range(len(li)):
    if isinstance(li[i], int):
        result *= int(li[i])
    else:
        flag = False

if flag:
    print(result)
else:
    print('에러발생')