t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    
    if 0 <= x <= 23 and 0 <= y <= 59:
        time = 'Yes'
    else:
        time = 'No'
    
    if 1 <= x <= 12:
        if x == 2 and 1 <= y <= 29:
            date = "Yes"
        elif x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31:
            date = "Yes"
        elif 1 <= y <= 30:
            date = "Yes"
        else:
            date = "No"
    else:
        date = "No"
    
    print(f'{time} {date}')