adress = list(input().split('/'))

print(f'protocol: {adress[0][:-1]}')
print(f'host: {adress[2]}')
print(f'others: {adress[3]}')