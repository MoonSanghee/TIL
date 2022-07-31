import sys

sys.stdin = open("1206_input.txt", "r")

test_case = 10

for test_num in range(1, test_case + 1):
    length = int(input())
    buildings = list(map(int, input().split()))
    
    view = 0

    for i in range(2, len(buildings) - 2):
        if buildings[i] == max(buildings[i - 2], buildings[i - 1], buildings[i], buildings[i + 1], buildings[i + 2]):
            view += buildings[i] - max(buildings[i - 2], buildings[i - 1], buildings[i + 1], buildings[i + 2])
    
    print(f'#{test_num} {view}')