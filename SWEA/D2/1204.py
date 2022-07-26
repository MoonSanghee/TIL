import sys

sys.stdin = open("1204_input.txt", "r")

t = int(input())
for i in range(1, t + 1):
    print(f'#{input()} ', end = '')
    point_list = list(map(int, input().split()))
    student_count = [0] * 101
    most_point = 0
    max_point = 0
    for j in point_list:
        student_count[j] += 1
    for k in range(101):
        if student_count[k] >= most_point:
            most_point = student_count[k]
            max_point = k
    print(max_point)