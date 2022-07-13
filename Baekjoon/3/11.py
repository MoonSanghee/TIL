# 3-11 몬제번호 10871

# Q. 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# A.
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < X:                  #end='index'는 출력 함수 마지막에 index를 넣어주겠다는 의미입니다.
#         print(A[i], end = " ")    #연속된 값 입력시 줄 바꿈 없이 입력 가능