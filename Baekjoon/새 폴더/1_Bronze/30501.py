n = int(input())
# 용의자의 수를 받아줍니다.
for _ in range(n):
    name = input()
    if 'S' in name:
        result = name
    # 이름을 확인하여 범인을 찾아줍니다.
    # 범인의 조건인 S가 포함된 이름이 유일하다고되어있으므로 
    # n개의 이름을 받으며 S가 들어가있는지 확인하여 바로 변수에 담아줍니다.

print(result)
# 범인의 이름을 출력해줍니다.