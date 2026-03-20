N = int(input())
# 주어지는 이름의 수를 받아줍니다
for i in range(N):
    x = i + 1
    first = input()
    last = input()
    # 성과 이름을 받아줍니다
    print(f'Case {x}: {last}, {first}')
    # 주어진 양식에 맞게 출력해줍니다