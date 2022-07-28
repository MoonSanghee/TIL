test_case = int(input())

for i in range(test_case):
    N, M = map(int, input().split())
    number_seet = []
    for line in range(N):
        each_line = list(map(int, input().split()))
        number_seet.append(each_line)
    