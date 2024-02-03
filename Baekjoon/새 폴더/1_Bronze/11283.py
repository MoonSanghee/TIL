word = input()
# 단어를 받아줍니다.
idx = ord(word) - ord("가") + 1
# ord함수를 이용하여 입력받은 단어가 몇번째 단어인지 확인해줍니다.
print(idx)
# idx값을 출력해줍니다