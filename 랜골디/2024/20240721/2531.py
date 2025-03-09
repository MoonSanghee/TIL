n, d, k, c = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
# 주어지는 접시수, 가짓수, 연속해서 먹는 접시, 쿠폰을 받아주고 놓여있는 접시들을 받아줍니다.
numbers += numbers
# 회전초밥이기때문에 마지막 접시 다음에는 다시 맨 처음 접시가 오기때문에 접시의 배열을 2번 반복해줍니다.
result = 0
# 결과를 담을 변수를 설정해줍니다
for i in range(n):
    pic = numbers[i:i + k]
    cnt = len(set(pic))
    # 각 자리에서 연속한 k개의 초밥의 종류를 확인하여줍니다.
    if c not in pic:
        cnt += 1
    # 선택한 초밥에 쿠폰으로 먹을 초밥이 존재하는지 확인해줍니다.
    result = max(result, cnt)
    # result값을 갱신해줍니다.

print(result)
# 결과를 출력해줍니다.