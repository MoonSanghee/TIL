s = input()
# 주어지는 문자열을 받아줍니다
looking = "KOREA"
idx = 0
# 반복되도록할 문자열을 담고 문자열의 어떤 문자가 와야하는지 idx를 정해줍니다
result = ''
# 완성된 문자열을 담을 변수를 설정해줍니다
for i in s:
    if i == looking[idx]:
        result += i
        idx = (idx + 1) % 5
# 주어진 문자열을 순회하며 반복되는 문자열에 추가될 문자라면 result에 추가해줍니다.
print(len(result))
# 반복하는 문자열의 길이를 출력해줍니다