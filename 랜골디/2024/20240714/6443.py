n = int(input())
# 입력받을 단어의 개수를 받아줍니다.
def anagram(new):
    if len(new) == len(word):
        print(new)
        return
    # 에너그램으로 만든 단어가 주어진 단어의 길이와 같아지면 출력해줍니다.
    for i in range(len(word)):
        if visited[i] == False:
            # 단어를 순회하면서 사용된적없었다면
            if new + word[i] not in made[len(new) + 1]:
                # 문자를 추가하였을때 그 길이의 단어중 만들어 진적이 없는 조합인지 확인하고
                visited[i] = True
                made[len(new) + 1].add(new + word[i])
                anagram(new + word[i])
                visited[i] = False
                # 만들어진적이 없다면 그 길이 만큼의 단어에 추가하고 재귀를 통해 새 단어를 찾아줍니다.


for _ in range(n):
    word = list(input())
    word.sort()
    # 단어를 리스트에 입력받고 정렬해줍니다.
    made = [set() for _ in range(20)]
    # 주어지는 단어의 최대 길이가 20이므로 길이가 20인 단어까지 담을수 있도록 20개의 set을 가지는 리스트를 만들어줍니다.
    visited = [False for _ in range(len(word))]
    # 각 문자를 사용하였는지 확인할 리스트를 만들어줍니다.
    anagram('')
    # 함수를 실행시켜 에너그램을 만들어줍니다.