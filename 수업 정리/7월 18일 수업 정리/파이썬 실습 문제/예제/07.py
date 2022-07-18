# Q. 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# Ouput
# 5.5

# A.
# count 값이 전체를 순환한 다음 마지막에만 1이 더하는 구조로 코드가 짜여있다.
# number_list안의 값들을 total에 더해줄 때마다 count 값을 1씩 더해주기 위해
# 들여쓰기를 통해 'count += 1'이라는 문장도 반복문 안에 넣어주면
# total에 값을 추가할 때마다 count 값도 증가하여 올바른 분모 값을 구할 수 있고
# 마지막 줄 print(total // count) 를 print(total / count)로 바꾸어주면 
# 소수점 아래 값도 얻을 수 있다.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)