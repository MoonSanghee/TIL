li=[i+1 for i in range(20)]
# 카드 배치를 만들어줍니다.
for i in range(10):
    m, n = map(int, input().split())
    # 뒤집을 카드의 범위를 받아줍니다.
    a=li[:m-1]
    b=li[m-1:n][::-1]
    c=li[n:]
    li=a+b+c
    # 뒤집을 영역으로 값을 바꾸어 카드 배치를 갱신해줍니다.
    
print(*li)
# 카드 배열을 출력해줍니다.