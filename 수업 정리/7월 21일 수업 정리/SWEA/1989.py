T = int(input())

for i in range(T):
    a = input()
    for j in range(len(a)):
        if j == (len(a) - 1):
            print(f'#{i + 1} 1')
        elif a[j] == a[len(a)- j - 1]:
            continue
        else:
            print(f'#{i + 1} 0')
            break
