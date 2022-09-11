# 프로그래머스 - 이진 변환 반복하기
# 나의 풀이
def solution(s):
    cnt = 0
    zero = 0
    while s != '1':
        cnt += 1
        result = 0
        for i in s:
            if i == '0':
                zero += 1
            else:
                result += 1
        s = bin(result)[2::]
    answer = [cnt, zero]
    return answer

# 리뷰 포인트
# b = format(n, 'b')를 통해 주어진 정수를 2진수 형태로 변환하는 방법도 있음.