# Q. 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류 코드
# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

# Output
# {'Apricot': 1,
#  'Blackcurrant': 1,
#  'Cantaloupe': 1,
#  'Feijoa': 1,
#  'Grapefruit': 1,
#  'Juniper berry': 1,
#  'Salal berry': 1,
#  'Soursop': 1}

# A.
# 위의 코드에서 'fruit_count = {fruit: 1}'는 그 상황에서 fruit_count를 바꿔주지만
# for 이전에 값에 돌려보내 다시 저장하지 않아서 if 문이 반복되며 입력값이 누적되지 않고
# 덮어씌워져 마지막으로 들어오는 fruit 값인 Salal berry와 그에 대한 밸류값만 출력된다.
# 따라서 'fruit_count = {fruit: 1}'를 입력된 fruit값을 키 값으로 하고 
# value값을 1로 받도록 'fruit_count[fruit] = 1'처럼 바꾸어주면 원하는 결과를 받을 수 있다.

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)