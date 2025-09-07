n = int(input())
for _ in range(n):
    m = int(input())
    new = bin(m)[2:][::-1]
    if new.count('1') == 1:
        print(f'{len(new) - 2} {len(new) - 2}')
    else:
        for i in range(len(new)):
            if new[i] == '1':
                print(i, end = ' ')
        print()