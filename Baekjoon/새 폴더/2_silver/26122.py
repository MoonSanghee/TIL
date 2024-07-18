n = int(input())
sticks = input()
# 막대의 길이와 막대의 형태를 받아줍니다.
cnt = 1
magnets = [0]
# 연속하는 극의 길이를 담을 변수와 연속하는 영역을 담을 리스트를 만들어줍니다.
for i in range(1, n):
    if sticks[i - 1] == sticks[i]:
        cnt += 1
    else:
        magnets.append(cnt)
        cnt = 1
magnets.append(cnt)
# 연속하는 부분이 바뀌면 확인한 길이까지 리스트에 넣고 길이를 갱신해줍니다.
result = 0

for i in range(1, len(magnets)):
    result = max(result, min(magnets[i - 1], magnets[i]) * 2)
# 연속하는 막대의 길이를 비교하여 작은 극의 길이의 2배만큼 자석이 되므로 자석을 비교하여 값을 갱신해줍니다
print(result)
# 결과를 출력해줍니다.