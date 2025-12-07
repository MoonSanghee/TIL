n = int(input())
# 주어지는 수를 받아줍니다
s = "%.300f" % 2 ** - n
# 주어지는 소수를 구하여줍니다
end = len(s)
for i in range(end - 1, 1, -1):
    if s[i] != '0':
        end = i
        break
# 마지막부터 0이 아닌수까지 찾아줍니다
print(s[:end + 1])
# 결과를 출력해줍니다