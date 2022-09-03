acards = list(map(int, input().split()))
bcards = list(map(int, input().split()))
apoint = 0
bpoint = 0
result = []
for i in range(10):
    if acards[i] > bcards[i]:
        apoint += 3
        result.append('A')
    elif bcards[i] > acards[i]:
        bpoint += 3
        result.append('B')
    else:
        apoint += 1
        bpoint += 1
        result.append('D')
print(apoint, bpoint, end = ' ')
print()
if apoint > bpoint:
    print('A')
elif bpoint > apoint:
    print('B')
else:
    for i in range(10):
        if result[9 - i] == 'A':
            print('A')
            break
        elif result[9 - i] == 'B':
            print('B')
            break
        if i == 9:
            if result[0] =='D':
                print('D')