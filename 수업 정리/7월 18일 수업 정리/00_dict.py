word = 'banana'
result = {}
for char in word:
    # result[char] :없으면 KeyError
    # result.get(char, 0) #없으면 None, 기본값을 주면 기본값 출력
    result[char] = result.get(char, 0) + 1
    # if char not in result:
    #     result[char] = 1
    # else:
    #     result[char] = result[char] + 1
print(result)