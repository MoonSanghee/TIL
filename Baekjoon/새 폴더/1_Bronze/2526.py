n, p = map(int, input().split())

li = [] 
# 반복되는 숫자 저장할 배열 만들어줍니다
r = n 
# 나머지를 담을 변수를 만들어줍니다.

while True:
    r = (r * n) % p
    if r in li:
        print(len(li) - li.index(r))
        break
    li.append(r)
    # 반복되는 구간이 나올때까지 시행하여줍니다.