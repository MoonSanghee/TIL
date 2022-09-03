test_case = int(input())

for test in range(test_case):
    line = list(map(int, input().split()))
    line = sorted(line)
    print(line[-3])