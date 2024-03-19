cnt = [ 3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1 ]
result = []
A = input()
B = input()
# 각 문자의 횟수와 주어지는 입력을 받아줍니다.
for i in range(len(A)):
    result.append(int(cnt[ord(A[i])-65]))
    result.append(int(cnt[ord(B[i])-65]))
    # A와 B 글자의 획수를 차례대로 넣어줍니다.
while len(result) > 2:
    new = []
    for i in range(len(result) - 1):
        new.append((result[i] + result[i + 1])%10)
    result = new
    # 이웃한 두 수를 더하여 새 리스트를 만드는것을 2개의 숫자만 남을때까지 반복해줍니다

print(str(result[0]) + str(result[1]))
# 십의 자리가 0이어도 출력해야하므로 남은 두 수를 문자열 형태로 더하여 출력해줍니다.