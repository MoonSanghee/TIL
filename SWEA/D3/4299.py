import sys
sys.stdin = open('sample_input.txt')

# test = int(input())
# for t in range(1, test + 1):
#     dumped = list(map(int, input().split()))
#     bench = [11, 11, 11]
#     result = []
#     if dumped[0] < bench[0]:
#         print(f'#{t} -1')
#     elif dumped[0] == bench[0] and dumped[1] < bench[1]:
#         print(f'#{t} -1')
#     elif dumped[0] == bench[0] and dumped[1] == bench[1] and dumped[2] < bench[2]:
#         print(f'#{t} -1')
#     else:
#         for i in range(3):
#             result.append(dumped[i] - bench[i])
#         print(f'#{t} {result[0]*24*60 + result[1]*60 + result[2]}')


test = int(input())
for t in range(1, test + 1):
    dumped = list(map(int, input().split()))
    bench = [11, 11, 11]
    result = []
    for i in range(3):
        result.append(dumped[i] - bench[i])

    known = result[0]*24*60 + result[1]*60 + result[2]
    if known < 0:
        print(f'#{t} -1')
    else:
        print(f'#{t} {known}')