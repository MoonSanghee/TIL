import sys
input = sys.stdin.readline
N = int(input())
# 찾고자하는 소수의 자리수를 찾아줍니다
def addNumber(number):
    if number > 10 ** (N - 1):
        return print(number)
        # 만들어진 신기한 소수가 자릿수가 충분하다면 출력해줍니다
    for i in range(1, 10):
        new = number * 10 + i
        for j in range(2, int(new ** 0.5) + 1):
            if new % j == 0:
                break
        else:
            addNumber(new)
        # 자릿수가 부족하다면 주어진 신기한 소수를 이용해 만들어지는 신기한 소수를 찾아줍니다
for i in [2, 3, 5, 7]:
    addNumber(i)
    # 한자리수 소수인 2, 3, 5, 7을 이용해 각각의 소수로 시작하는 신기한 소수들을 찾아줍니다