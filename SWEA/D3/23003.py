T = int(input())
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
d = dict()
for i in range(6):
    d[color[i]] = i
# 테스트 케이스의 수를 받고 색의 배치를 딕셔너리에 담아줍니다

for _ in range(T):
    S, T = input().split()
    # 주어지는 두 색을 받아줍니다
    if S == T:
        print('E')
    elif abs(d[S] - d[T]) == 3:
        print('C')
    elif abs(d[S] - d[T]) == 1 or abs(d[S] - d[T]) == 5:
        print('A')
    else:
        print('X')
    # 두 색의 관계를 확인하여 출력해줍니다