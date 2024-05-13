n = int(input())
# 테스트 케이스의 수를 받아줍니다.
for _ in range(n):
    target, copy = input().split()
    # 만들 단어와 복사해둔 단어를 받아줍니다.
    result = len(target) - (len(copy) - 1) * target.count(copy)
    # 만들려는 단어의 길이에서 복사한 단어는 복사한 단어만큼의 입력 대신 1번의 입력이면 됩니다.
    print(result)
    # 필요한 입력횟수를 출력해줍니다.