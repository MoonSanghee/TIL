test_case = int(input())

for test in range(test_case):
    line = list(map(str, input().split()))
    for i in range(len(line)):
        line[i] = list(line[i])
        reline = (line[i])[::-1]
        for j in range(len(reline)):
            print(reline[j], end = '')
        print(end = ' ')
    print()

    # string = list(input().split())
    # for j in string:
    #     print(j[::-1], end = ' ')