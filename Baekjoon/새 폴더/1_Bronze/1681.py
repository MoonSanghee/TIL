n, l = input().split()
n = int(n)
# 주어지는 두 수를 문자열형태로 받고 n을 정수로 바꾸어줍니다
count = 1
number = 1
if l == '1':
    number += 1
# 붙인 번호가 몇번인지 담을 변수와 몇번째인지 담을 변수를 설정하고 피할 번호가 1이라면 붙일 번호를 2로 만들어줍니다
while n != count:
    # 목표에 도달할때까지 시행합니다
    number += 1
    if l in str(number):
        continue
    else:
        count += 1
    # 붙일 번호를 1씩 늘려 피할 번호가 있는지 확인하고 없을경우만 붙였다고 값을 갱신해줍니다

print(number)
# 결과를 출력해줍니다