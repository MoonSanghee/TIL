# 프로그래머스 - 전화번호 목록
def solution(numbers):
    answer = True
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1].startswith(numbers[i]):
            answer = False
            break
    return answer

# 정수형태의 숫자를 정렬하면 길이와 상관없이 정렬됨.
# 예를 들어 정수형이면 11이 9 보다 큰 숫자지만 문자형이면 '11'의 첫자리 1이 '9'의 첫자리보다 작으므로 11이 먼저 나오도록 정렬 됨.