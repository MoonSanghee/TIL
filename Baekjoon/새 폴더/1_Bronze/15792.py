a, b = map(int, input().split())
print(a // b, end = '') 
# 몫을 출력해줍니다.

if a % b: 
    # 나머지가 있다면
    print('.', end='') 
    i = 0
    # 점(.)을 출력해주고 소수점을 표시해줄 변수를 지정해줍니다.
    
    while a % b and i < 1000:
        # 계속 10씩 곱해주면서 몫을 뒤에 붙여줍니자.
        a = a % b * 10  
        i += 1
        print(a // b, end = '')