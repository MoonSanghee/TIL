n = int(input())
# 수를 받아줍니다.

cnt = 0  
# 박수 친 횟수를 담을 변수를 정해줍니다.
for num in range(1, n+1):
    for i in str(num):
        if i == '3' or i == '6' or i == '9':
            cnt += 1
    # 모든 수의 자릿수를 확인하여 3, 6, 9중에 하나이면 박수를 1회 쳤음을 표시해줍니다.
        
print(cnt)
# 박수친 횟수를 출력해줍니다.