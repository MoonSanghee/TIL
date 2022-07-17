# 5-3 문제번호 1065

# Q. 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# input
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# output
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# A.
a = int(input())
cnt = 0
for i in range(1, a + 1):
    if i < 100:
        cnt += 1
    else:
        l = []
        for j in str(i):
            l.append(j)
        if int(l[0]) - int(l[1]) == int(l[1]) - int(l[2]):
            cnt += 1
print(cnt)

# 찾아본 풀이
# num = int(input())

# hansu = 0
# for i in range(1, num+1):
#     num_list = list(map(int, str(i)))
#     if i < 100:
#         hansu += 1  # 100보다 작으면 모두 한수
#     elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#         hansu += 1  # x의 각 자리가 등차수열이면 한수
# print(hansu)