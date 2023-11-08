def solution(today, terms, privacies):
    answer = []
    new_terms = dict()
    for term in terms:
        term_type, term_period = term.split()
        term_period = int(term_period)
        limit = list(map(int, today.split('.')))
        limit[1] -= term_period
        while limit[1] <= 0:
            limit[1] += 12
            limit[0] -= 1
        new_terms[term_type] = limit
    for num in range(len(privacies)):
        privacy = privacies[num]
        privacy_date, privacy_type = privacy.split()
        privacy_date = list(map(int, privacy_date.split('.')))
        limit_date = new_terms[privacy_type]
        print(limit_date, privacy_date)
        if limit_date[0] > privacy_date[0]:
            answer.append(num + 1)
        elif limit_date[0] == privacy_date[0]:
            if limit_date[1] > privacy_date[1]:
                answer.append(num + 1)
            elif limit_date[1] == privacy_date[1]:
                if limit_date[2] >= privacy_date[2]:
                    answer.append(num + 1)
    return answer