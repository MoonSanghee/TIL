n = int(input())
names = [input() for _ in range(n)]
# 이름의 개수와 이름들을 받아줍니다.
D = sorted(names, reverse=True)
I = sorted(names)
# 오름차순 정렬한 형태와 내림차순 형태를 만들어줍니다.
if names == D:
    print("DECREASING")
elif names == I:
    print("INCREASING")
else:
    print("NEITHER")
    # 주어진 리스트가 오름차순 혹은 내림차순인지 확인하고 결과를 출력해줍니다.