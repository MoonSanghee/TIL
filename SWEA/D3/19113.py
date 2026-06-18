T = int(input())
# 테스트케이스의 개수를 받아줍니다
for t in range(T):
    N = int(input())
    tags = list(map(int, input().split()))
    result = []
    # 주어지는 가격표의 개수와 가격표들을 받고 결과를 담을 변수를 설정해줍니다
    while tags:
        x = tags[0]
        result.append(str(x))
        tags.remove(x * 4 // 3)
        tags.remove(x)
    # 가격표를 차례대로 확인하며 할인 전 가격과 확인한 가격표를 제거해줍니다
    result = ' '.join(result)
    print(f'#{t + 1 } {result}')
    # 할인한 가격표들을 주어진 양식에 맞게 출력해줍니다