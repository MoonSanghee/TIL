tc = int(input())
# 테스트 케이스의 수를 받아줍니다.
for t in range(tc):
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    # 수의 개수를 받고 학번을 받아줍니다.
    if n == 1:
        print(1)
    else:
        cnt = 2
        while True:
            result = set()
            for i in range(n):
                result.add(numbers[i] % cnt)
            if len(numbers) == len(result):
                print(cnt)
                break
            else:
                cnt += 1
        # 학번이 둘이상이라면 2부터 모든 학번을 나눴을때 나머지가 학번의 종류와 같은 경우를 찾아 출력해줍니다.