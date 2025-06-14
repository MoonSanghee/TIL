while True:
    n, k = map(int, input().split())
    # 주어지는 수열의 길이와 사촌을 찾을 수를 받아줍니다
    if n == k == 0:
        break
    # 입력된 두 수가 모두 0이라면 마지막 입력이므로 실행을 멈추어줍니다
    numbers = list(map(int, input().split()))
    # 주어지는 수열을 받아줍니다
    trees = dict()
    trees[numbers[0]] = 0
    # 트리를 담을 딕셔너리를 만들고 루트노드를 담아줍니다
    idx = -1
    # 수열의 어떤 수에 아래에 추가될 노드인지 idx을 확인할 변수를 설정해줍니다
    for i in range(1, n):
        if numbers[i] == numbers[i - 1] + 1:
            trees[numbers[i]] = numbers[idx]
            # 지금 수가 연속한 수라면 이전과 같은 부모노드를 가집니다
        else:
            idx += 1
            trees[numbers[i]] = numbers[idx]
            # 수열에서 연속하지 않는 수가 나왔다면 수열의 다음 인덱스의 값을 부모로 가지게 해줍니다
    
    if trees[k] == numbers[0]:
        print(0)
        # 부모 노드가 루트 노드라면 사촌이 존재할 수 없습니다
    else:
        result = 0
        # 사촌의 수를 담을 변수를 설정해줍니다
        for i in range(1, n):
            parent = trees[numbers[i]]
            if parent != trees[k] and trees[parent] == trees[trees[k]]:
                result += 1
                # 부모노드가 다르고 부모노드의 부모노드가 같은 것이 몇개인지 찾아줍니다
        print(result)
        # 결과를 출력해줍니다