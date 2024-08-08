n = int(input())
# 주어지는 수를 받아줍니다.
result = 0
# 1 빼기를 몇번 실행하였는지 담을 변수를 설정해줍니다.
while n:
    number = str(n)
    # 수를 문자열 형태로 변환해줍니다.
    result += number.count('1')
    n = int('0' + number.replace('1', ''))
    # result에 문자열 '1'의 개수를 확인하여 그 개수만큼 더해주고 '1'을 전부 없앤후 n 값을 갱신해줍니다.
    if n:
        n -= 1
        result += 1
    # n이 0이 아니라면 숫자 1을 빼고 1빼기를 실행하였음을 더해줍니다.

print(result)
# 1빼기를 실행한 횟수를 출력해줍니다.