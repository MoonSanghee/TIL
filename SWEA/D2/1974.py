import sys

sys.stdin = open("1974_input.txt", "r")

test_case = int(input())


check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for test_num in range(1, test_case + 1):
    seet = []
    break_check = 0

    for i in range(9):
        line = list(map(int, input().split()))
        seet.append(line)


    for i in range(9):
        each_line = sorted(seet[i])
        if each_line != check_list:
            print(f'#{test_num} 0')
            break_check = 1
            break

        stripe = []
        for j in range(9):
            stripe.append(seet[j][i])
        
        stripe_line = sorted(stripe)
        if stripe_line != check_list:
            print(f'#{test_num} 0')
            break_check = 1
            break
    
    if break_check == 0:
        for i in range(3):
            for j in range(3):
                miniseet = []
                if break_check == 0:
                    for i2 in range(3):
                        for j2 in range(3):
                            miniseet.append(seet[(i * 3) + i2][(j * 3) + j2])
                    miniseet = sorted(miniseet)
                    if miniseet != check_list:
                        print(f'#{test_num} 0')
                        break_check = 1
                        break

    if break_check == 0:
        print(f'#{test_num} 1')