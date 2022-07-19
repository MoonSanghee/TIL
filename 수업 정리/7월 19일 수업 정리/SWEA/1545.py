# Q. 주어진 숫자부터 0까지 순서대로 찍어보세요


a = int(input())
for i in range(a + 1):
    print(a - i, end = ' ')