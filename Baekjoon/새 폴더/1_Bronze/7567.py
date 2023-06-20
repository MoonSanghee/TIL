plates = input()
# 그릇이 놓인 형태를 받아줍니다.
result = 10
# 높이를 저장할 변수를 정해줍니다.
before = plates[0]
# 이전 그릇의 형태를 저장할 변수를 정해줍니다.
for i in range(1, len(plates)):
    # 1번 인덱스의 그릇부터 차례대로
    if before != plates[i]:
        before = plates[i]
        result += 10
        # 이전에 놓인 그릇과 방향이 다르다면 이전의 그릇 형태를 바꾸어주고
        # result를 10 더해주고
    else:
        result += 5
        # 아니라면 5 더해줍니다.

print(result)
# result의 값을 출력해줍니다.