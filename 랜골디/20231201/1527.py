s, e = map(int, input().split())

total = []

def check(num):
    if int(num + '4') < s:
        total.append(num + '4')
        check(num + '4')
    if int(num + '7') < s:
        total.append(num + '7')
        check(num + '7')

check('')

total2 = []

def check2(num):
    if int(num + '4') <= e:
        total2.append(num + '4')
        check2(num + '4')
    if int(num + '7') <= e:
        total2.append(num + '7')
        check2(num + '7')

check2('')

print(len(total2) - len(total))