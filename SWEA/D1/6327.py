numbers = list(map(int, input().split(',')))

for i in numbers:
    print(f'square({i}) => {i * i}')
    # 주어지는 수들을 받아 제곱값을 구하여 주어진 양식에 맞게 출력해줍니다