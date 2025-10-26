n = int(input())
s = input()
# 주어지는 변수를 받아줍니다
arr = []
for i in range(n):
    if s[i] == 'A':
        arr.append(i)
# A의 위치를 구하여줍니다
result = 0
# 결과를 담을 변수를 설정해줍니다
if len(arr) <= 1:
    print(0)
# A의 개수가 1이하라면 0을 출력해줍니다
else:
    for i in range(1, len(arr)):
        if s[arr[i - 1]:arr[i]].count("A") == 1 and s[arr[i - 1]:arr[i]].count("N") == 1:
            result += 1
    print(result)
    # 주어진 조건에 맞는 단어의 개수를 찾아 출력해줍니다