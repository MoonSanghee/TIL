T = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for i in range(T):
    N = int(input())
    if N <= 25:
        print(f'Case #{i + 1}: World Finals')
    elif N <= 1000:
        print(f'Case #{i + 1}: Round 3')
    elif N <= 4500:
        print(f'Case #{i + 1}: Round 2')
    else:
        print(f'Case #{i + 1}: Round 1')
# 주어진 입력에 따른 결과를 출력해줍니다