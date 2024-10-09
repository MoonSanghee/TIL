while True:
    n = int(input())
    if n == 0:
        break
    # 학생수가 0이 될때까지 실행해줍니다.

    tall = 0
    name = []
    # 키와 학생들의 이름을 담을 리스트를 만들어줍니다.
    for _ in range(n):
        student, height = input().split()
        height = float(height)
        if height > tall:
            tall = height
            name = [student]
        # 키가 이전에 최장신보다 크다면 키값을 갱신하고 리스트도 갱신해줍니다.
        elif height == tall:
            name.append(student)
        # 키가 이전의 최장신과 같다면 이름을 추가해줍니다.
    
    print(*name)
    # 최장신인 명단을 출력해줍니다.