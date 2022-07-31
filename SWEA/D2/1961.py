import sys

sys.stdin = open("1961_input.txt", "r")

test_case = int(input())

for test_num in range(1, test_case + 1):
    print(f'#{test_num}')
    
    n = int(input())
    seet = []
    for i in range(n):
        line = list(map(int, input().split()))
        seet.append(line)
    

    for i in range(n):
        turn_90, turn_180, turn_270 = '', '', ''
        for j in range(n):
            turn_90 += str(seet[n - 1 - j][i])
            turn_180 += str(seet[n - 1 - i][n -1 - j])
            turn_270 += str(seet[j][n - 1 - i])


        
        print(turn_90, turn_180, turn_270)