code = input()
# 주어지는 입력을 받아줍니다
flag = True
# 동아리비를 횡령할수 있는지 담을 변수를 설정해줍니다
for i in code:
    if i not in '1234567890+':
        flag = False
# 숫자와 +이외의 문자가 있다면 횡령이 불가합니다
if code.count('+') != 1:
    flag = False
    # +가 1개가 아니라면 횡령이 불가합니다
else:
    a, b = code.split('+')
    if a == '' or a[0] == '0' or a != b:
        flag = False
# 두 수가 조건에 부합하지 않으면 횡령이 불가합니다
if flag:
    print("CUTE")
else:
    print("No Money")
# 확인한 결과를 출력해줍니다