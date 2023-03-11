n = int(input())
numbers = [str(input()) for _ in range(n)]
# 학생 번호의 개수와 번호들을 받아줍니다.
# 이 때 학생번호는 자리수를 이용하기위해 문자열 형태로 받아줍니다.
for i in range(len(numbers[0])):
    had = set()
    for j in range(n):
        if numbers[j][-i - 1:] in had:
            break
        else:
            had.add(numbers[j][-i-1:])
    # 각 자리수를 확인하며 나온적 있는지 확인하기위해 담아줄 set 자료형을 만들어줍니다.
    # numbers 각 값들을 확인하며 나온적 없다면 set에 넣어주고 있다면 다음 자리수를
    # 확인해줍니다.
    else:
        print(i + 1)
        break
    # 모든 수를 확인하여 반복되는 값이 없는 자리수가 나타났을때 값을 출력해줍니다.