a, check, b = input().split()
# 주어지는 불리언값과 연산을 받아줍니다
if check == "AND":
    if a == b and a == "true":
        print("true")
    else:
        print("false")
else:
    if a == b and a == "false":
        print("false")
    else:
        print("true")
# 주어지는 값에 따라 참거짓을 확인하여 결과값을 출력해줍니다