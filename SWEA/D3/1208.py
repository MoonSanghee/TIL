import sys

sys.stdin = open("1208_input.txt", "r")

test_case = 10

for test_num in range(1, test_case + 1):

    dump = int(input())

    boxes = list(map(int, input().split()))

    while dump > 0:
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1
        dump -= 1

    print(f'#{test_num} {max(boxes) - min(boxes)}')