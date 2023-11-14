n = int(input())
numbers = [int(input()) for _ in range(n)]
# 수의 개수와 가진 수들을 받아 리스트에 담아줍니다.
length = len(numbers)
result = 5
# 수열의 길이와 필요한 수의 개수를 담을 변수를 정해줍니다.
for i in numbers:
    need = 4
    # 수가 잇다면 추가로 필요한 수는 4개이므로 4개가 필요하다 설정해줍니다.
    for j in range(1, 5):
        if i + j in numbers:
            need -= 1
    # 수를 기준으로 1부터 4까지를 더해 i부터 시작한 올바른 배열중 몇개가 부족한지 확인해줍니다.
    result = min(result, need)
    # result값과 비교하여 더 적게 필요한지 확인해줍니다.
print(result)
# result의 값을 출력해줍니다.