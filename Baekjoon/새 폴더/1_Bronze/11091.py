n = int(input())

for _ in range(n):
    line = input().lower()

    result = ''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in line:
            result += i
    
    if result == '':
        print('pangram')
    else:
        print(f'missing {result}')
    # 문장을 입력받아 모든 알파벳을 포함하는지 확인하여 주어진 형식대로 결과를 출력해줍니다