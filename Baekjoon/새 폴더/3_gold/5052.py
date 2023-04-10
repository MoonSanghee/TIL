import sys
input = sys.stdin.readline

t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    n = int(input())
    # 확인할 번호의 수를 받아줍니다.
    numbers = [str(input().strip()) for _ in range(n)]
    numbers.sort()
    # 입력받는 전화번호를 문자열로 받아 리스트에 넣어주고
    # 번호가 담긴 리스트를 내림차순으로 정렬해줍니다.
    result = True
    # 일관성이 있다고 기본 형태를 잡아줍니다.
    for i in range(n - 1):
        # 연속한 두 번호를 비교할것이기 때문에 n - 1위치의 인덱스까지 확인이 가능합니다.
        length = len(numbers[i])
        if numbers[i] == numbers[i + 1][:length]:
            result = False
            break
            # numbers[i]의 길이가 length라고 할 때
            # numbers[i + 1]의 앞에서부터 length의 길이 문자열이 numbers[i]와 같다면
            # 연속하지 않으므로 표시해주고 반복을 멈춥니다.
    if result:
        print('YES')
    else:
        print('NO')
        # 연속하다면 'YES'아니면 'NO'를 출력해줍니다.