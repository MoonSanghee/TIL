# Q. 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# numbers = input().split()
# print(sum(numbers))

# Input
# 10 20

# Output
# 30

# A.
# sum 함수를 활용하려면 입력값이 순환할 수 있는 구조로 되어 있어야하는데 
# 정의된 numbers는 입력된 값을 문자열 타입으로 연속하여 받을 뿐 입력된 값들 전체를 순환하지 못한다.
# 따라서 sum 함수를 써서 입력된 값을 받기 위해서는 numbers를 리스트 형태로 바꾸어 주어야 한다.

numbers = list(map(int, input().split()))
print(sum(numbers))