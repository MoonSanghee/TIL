t = int(input())
# 주어지는 테스트케이스가 몇개인지 받아줍니다
for _ in range(t):
    word, i, j = input().split()
    i, j = int(i), int(j)
    # 주어지는 단어와 단어의 제거할 범위를 받아줍니다
    result = word[:i] + word[j:]
    print(result)
    # 주어진 제거할 부위를 없앤 결과를 출력해줍니다