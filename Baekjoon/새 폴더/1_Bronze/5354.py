n = int(input())
# 박스의 갯수를 받아줍니다.
for _ in range(n):
    j = int(input())
    # 박스의 크기를 받아줍니다.
    for i in range(j):
        if i == j - 1 or i == 0:
            print('#'*j)
        else:
            print('#' + 'J' * (j - 2) + '#')
    # 박스를 출력합니다.
    print()
    # 박스를 출력한 다음 한 줄을 띄워줍니다.