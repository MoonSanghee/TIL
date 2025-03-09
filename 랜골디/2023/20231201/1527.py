s, e = map(int, input().split())
# 시작할 범위와 끝 범위를 받아줍니다.
total = []
# 시작점까지 금민수를 담을 리스트를 만들어줍니다.
def check(num):
    if int(num + '4') < s:
        total.append(num + '4')
        check(num + '4')
    if int(num + '7') < s:
        total.append(num + '7')
        check(num + '7')
# s 미만의 금민수를 리스트에 담아줍니다.

total2 = []

def check2(num):
    if int(num + '4') <= e:
        total2.append(num + '4')
        check2(num + '4')
    if int(num + '7') <= e:
        total2.append(num + '7')
        check2(num + '7')
# e 이하의 금민수를 리스트에 담아줍니다.

check('')
check2('')

print(len(total2) - len(total))
# e이하의 금민수의 개수에서 s미만의 금민수의 개수를 뺀 값을 출력해줍니다.