n = int(input())
# 결과를 받아줍니다
for i in range(65):
    number = (2 ** i - 1) * (2 ** (64 - i))
    if n == number:
        print(i)
        break
    # 틀린자리수별로 결과를 차례대로 확인하며 일치하는 값이 나오면 출력해줍니다.