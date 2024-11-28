tc = int(input())
# 테스트 케이스의 개수를 받아줍니다
for t in range(tc):
    n = int(input())
    l1 = list(input().split())
    l2 = list(input().split())
    looking = list(input().split())
    # 주어지는 문장의 길이를 받고 공개키1과 공개키 2, 암호문을 받아줍니다
    result = ['' for _ in range(n)]
    # 결과를 담을 리스트를 만들어줍니다
    for i in range(n):
        idx = l2.index(l1[i])
        result[i] = looking[idx]
    # 문장 2가 만들어진 과정을 확인하며 암호문을 평문으로 변환시켜줍니다
    print(*result)
    # 결과를 출력해줍니다