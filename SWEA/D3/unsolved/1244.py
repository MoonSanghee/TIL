import sys
sys.stdin = open('1244_input.txt', 'r')

test_case = int(input())
for test in range(1, test_case + 1):
    num, change = map(str, input().split())
    change = int(change)
    num = list(map(int, num))
    # while change:
    #     for i in range(len):
    
    
    print(num)


