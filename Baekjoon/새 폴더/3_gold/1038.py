n = int(input())

num = '0123456789'

cnt = 1

nums = []
for i in num:
    nums.append(i)
# nums에 1자리 감소하는수인 한자리 정수를 모두 넣어줍니다.

while cnt < 10:
    # 자릿수가 같아도 안 되고 모든 자리 수가 감소해야하므로 가장 큰 감소하는 수는
    # 9876543210입니다. 따라서 자릿수가 10 이하인 경우로 조건을 제한하여 while 
    # 반복문을 시행해줍니다.
    for i in nums:
        if len(i) == cnt:
            # nums를 순회하며 cnt의 길이와 같으면
            for j in range(10):
                if int(i[-1]) > j:
                    nums.append(i + str(j))
                    # 마지막 값보다 작을 수를 차례롤 더하여 리스트에 추가해 줍니다.
    cnt += 1
    # cnt를 1 더해 자릿수가 바뀌었음을 표시해줍니다.

if n > 1022:
    print(-1)
    # 총 감소하는 수의 개수는 1022개 존재하므로 그보다 큰 입력이 주어지면 -1을 출력하고
else:
    print(nums[n])
    # 1022 이하의 수가 주어지면 리스트에서 주어진 숫자의 인덱스 값을 출력해줍니다.