while True:
    command = list(input().split())
    if command[0] == '#' and command[1] == '0' and command[2] == '0':
        break
    if int(command[1]) > 17 or int(command[2]) >= 80:
        print(command[0], 'Senior')
    else:
        print(command[0], 'Junior')