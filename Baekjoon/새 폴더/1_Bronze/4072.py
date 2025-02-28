while True:
    line = list(input().split())
    if line == ['#']:
        break
    new = ''
    for word in line:
        new += word[::-1]
        new += ' '
    print(new)