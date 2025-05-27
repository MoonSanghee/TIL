ISBN = input()
result = 0
multiple = 0
# 주어지는 코드와 가려지지 않은 구간을 확인한 값과 가려진 구간의 가중치를 담을 변수를 설정해줍니다
for i in range(len(ISBN)):
    if ISBN[i] == '*':
        if i % 2:
            multiple = 3
        else:
            multiple = 1
    else:
        if i % 2:
            result += 3 * int(ISBN[i])
        else:
            result += int(ISBN[i])
    # 가려진 구간이라면 가중치를 표시하고 아니라면 가중치를 곱해 result에 더해줍니다

for i in range(10):
    if (result + (i * multiple)) % 10 == 0:
        print(i)
        break
    # 0부터 9까지의 수를 확인하며 가중치를 곱해 result에 더한 값이 0이 되는 값을 찾아 출력해줍니다