fruit = ['   apple    ','banana','  melon']
d = dict()
for i in fruit:
    i = i.strip()
    d[i] = len(i)
    
print(d)