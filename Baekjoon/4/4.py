# 4-4 문제번호 3052

# Q. 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1000보다 작거나 같고, 음이 아닌 정수이다.

# A1. 리스트를 set형태로 변환하여 길이 구하기
# a = 0
# b = []
# while a != 10:
#     a += 1
#     b.append(int(input())%42)
# b = set(b)
# print(len(b))

#while a != 10:은
# for i in range(10):과 동일

# A2. 입력한 10개의 숫자를 42로 나눈 나머지중 중복된 값을 제외한 새로운 리스트 만들어 길이 구하기
# a = 0
# b = []
# while a != 10:
#     a += 1
#     b.append(int(input())%42)
# b2 = []
# for i in b:
#     if i not in b2:
#         b2.append(i)
# print(len(b2))