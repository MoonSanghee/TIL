def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
    # 리무브를 이용하여 값을 사용한 값을 지우고 갱신 해줄 수 있음
    # maxlen을 통해 deque의 최대 길이를 설정할 수 있음.