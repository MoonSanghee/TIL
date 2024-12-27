while True:
    n = input().lower()
    if n == "#":
        break
    # 단어를 받아마지막줄인가 확인합니다.
    result = set()
    for i in n:
        if i.isalpha():
            result.add(i)
    # 단어를 순회하면 알파벳이라면 set자료형에 넣어줍니다
    print(len(result))
    # set자료형에 알파벳의 종류가 몇개인지 출력해줍니다.