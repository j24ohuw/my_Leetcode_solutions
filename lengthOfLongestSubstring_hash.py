def length(s):
    d = dict.fromkeys(set(s),-1)
    sequence = []
    for index, char in enumerate(s):
        if d[char] != -1:   d = dict((k, -1 if v < d[char] else v) for k,v in d.items())
        d[char] = index
        sequence.append([min(i for i in d.values() if i >= 0), max(d.values())])
    return max([i[1]-i[0]+1 for i in sequence]) if len(s) > 1 else (1 if len(s) == 1 else 0)
