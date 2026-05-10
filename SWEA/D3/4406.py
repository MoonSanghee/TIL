tc = int(input())

for t in range(tc):
    word = input()
    result = ''

    for i in word:
        if i not in 'aeiou':
            result += i
    
    print(f'#{t + 1} {result}')