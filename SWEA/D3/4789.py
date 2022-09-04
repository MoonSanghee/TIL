test = int(input())
for t in range(1, test + 1):
    audience = list(map(int, str(input())))
    clap = 0
    need = 0
    for i in range(len(audience)):
        if audience[i] != 0 and i > clap:
            need += i - clap
            clap = i
        clap += audience[i]
    print(f'#{t} {need}')