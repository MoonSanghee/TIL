import sys
input = sys.stdin.readline

t = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(t):
    R, A = 0, 0
    # 인식률과 전체 문자의 수를 확인할 변수를 설정해줍니다
    while True:
        line = input().strip()

        if line == '':
            break
        # 입력받은 문장이 공백 줄바꿈일때까지 받아줍니다
        for char in line:
            A += 1
            if char != '#':
                R += 1
        # 문장의 문자를 인식할 수 있는지를 확인하여 변수를 갱신해줍니다
        
    result = round(R / A * 100, 1)
    # 소수점 2번째에서 반올림하여줍니다
    if str(result).split('.')[-1] == '0':
        result = int(result)
    # 나누어 떨어진다면 정수형으로 바꿔줍니다
    print(f'Efficiency ratio is {result}%.')
    # 결과를 출력해줍니다