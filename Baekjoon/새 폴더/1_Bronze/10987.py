word = input()
# 문자를 입력받아줍니다.
gather = 'aeiou'
# 모음을 설정해줍니다.
count = 0
# 모음의 개수를 저장할 변수를 만들어줍니다.

for letter in word:
    if letter in gather:
        count += 1
# 문자를 순회하며 모음이 나오면 count에 값을 1 더해줍니다.
print(count)
# count에 저장된 값을 출력해줍니다.