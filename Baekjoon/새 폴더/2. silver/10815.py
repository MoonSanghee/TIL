# n = int(input())
# n_numbers = set(map(int, input().split()))
# m = int(input())
# m_numbers = list(map(int, input().split()))
# for i in m_numbers:
#     if i in n_numbers:
#         print(1, end = ' ')
#     else:
#         print(0, end = ' ')
# n 리스트에는 중복값이 없다. 따라서 리스트 형태를 확인하나 세트 형태를 확인하나 같은 값들에
# 대하여 존재 유무를 비교할 수 있으나 set에 특정 값이 있는지 확인 하는것은 O(1)의 시간값이 필요하고
# 리스트에서는 O(N)의 시간이 필요하다. 따라서 세트 형태의 n개의 숫자들에 대하여 비교해주면 훨씬 빨리 답을 구할 수 있다.

n = int(input())
N = list(map(int, input().split()))
N = sorted(N)
m = int(input())
M = list(map(int, input().split()))

for i in M:
    low, high = 0, n - 1
    check = 0
    while low <= high:
        mid = (low + high) // 2
        if N[mid] > i:
            high = mid - 1
        elif N[mid] < i:
            low = mid + 1
        else:
            check = 1
            break
    print(check, end = ' ')
