glade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

test = int(input())
for time in range(1, test + 1):
    students, found_student = map(int, input().split())

    new_glade = []
    for i in glade:
        for j in range(students//10):
            new_glade.append(i)

    point_list = []

    for i in range(students):
        mid_test, final_test, assign = map(int, input().split())
        point = mid_test * 0.35 + final_test * 0.45 + assign * 0.2
        point_list.append(point)

    point_rank = sorted(point_list, reverse=True)

    print(f'#{time} {new_glade[point_rank.index(point_list[found_student - 1])]}')
