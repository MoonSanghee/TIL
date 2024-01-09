n = int(input())
# 코드의 수를 받아줍니다.
def sum_number(word):
    result = 0
    for i in word:
        if i in '0123456789':
            result += int(i)
    return result
# 코드에 있는 수의 합을 구하는 함수를 만들어줍니다.
arr = [input() for _ in range(n)]
# 코드를 받아줍니다.
arr.sort(key = lambda x:(len(x), sum_number(x), x))
# lambda를 이용하여 길이, 숫자합, 사전순으로 정렬해줍니다.
for i in arr:
    print(i)
# 정렬한 코드를 차례대로 출력해줍니다.