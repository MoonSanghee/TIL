d = {
    "TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000,
}

li = []

for i in d:
    li.append((i, d[i]))

li.sort(lambda x: x[1],reverse = True)

for i in li:
    print(i[0] + ': ' + str(i[1]))