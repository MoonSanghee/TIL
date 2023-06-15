S = sum(list(map(int, input().split())))
T = sum(list(map(int, input().split())))
# 민국이와 만세의 점수를 받아 합친값을 변수에 저장하여줍니다.
if T > S:
    print(T)
    # 만세의 총점이 크다면 T에 저장된 값을 출력하고
else:
    print(S)
    # 아니라면 S에 저장된 값을 출력해줍니다.