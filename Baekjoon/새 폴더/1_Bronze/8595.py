import sys
input = sys.stdin.readline
n = int(input())
password = input()
# 단어의 길이와 단어를 받아줍니다.

onlyNumbers = ''
# 번호만 남겨 담을 변수를 정해줍니다.

for i in password:
    if i in '0123456789':
        onlyNumbers += i
    else:
        onlyNumbers += ' '
    # 숫자가 아니라면 ' '을 숫자면 그대로 변수에 넣어줍니다.
numbers = list(map(int, onlyNumbers.split()))
# 공백을 기준으로 나누어 정수로 변환시켜 리스트에 담아줍니다.
print(sum(numbers))
# 히든 넘버의 합을 출력해줍니다.