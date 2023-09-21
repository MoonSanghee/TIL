n = input()
arr = list(n)
# 수를 받아줍니다.
for i in range(1, len(arr)):
    num1 = 1
    num2 = 1
    # 연속하는 앞의 수의 곱과 뒤 수의 곱을 저장할 변수를 지정해줍니다.
    for j in range(i):
        num1 *= int(arr[j])
    for k in  range(i, len(arr)):
        num2 *= int(arr[k])
    # num1과 num2에 각각 연속한 자리수를 곱해줍니다.
    if num1 == num2:
        print('YES')
        break
    # 두 수가 같다면 'YES'를 출력해줍니다.
else:
    print('NO')
# 연속한 수의 곱이 같은 경우가 없다면 'NO'를 출력해줍니다.