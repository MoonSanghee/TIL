a = input()
count = 0
for i in a:    
    if i == '@':
        count += 1
    elif i == '(':
        print(count, end = ' ')
        count = 0
print(count)
