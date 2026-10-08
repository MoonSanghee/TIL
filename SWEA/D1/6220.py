n = int(input())

for i in range(n):
    i += 1
    j = input()
    if j.isupper():
        print(f'#1 {j} 는 대문자 입니다.')
    else:
        print(f'#1 {j} 는 소문자 입니다.')