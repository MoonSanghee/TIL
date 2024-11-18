n = int(input())
# 정수를 받아줍니다
new = bin(n)[2:]
re = new[::-1]
# 정수를 2진수로 전환하고뒤집어줍니다
number = int(re, 2)
# 뒤집은 2진법수를 정수로 바꾸어줍니다
print(number)
# 결과를 출력해줍니다