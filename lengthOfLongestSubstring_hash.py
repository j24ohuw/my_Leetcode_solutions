def length(s):

    d = dict.fromkeys(set(s),-1)
    sequence = []
    for index, char in enumerate(s):
        if index != 0:      sequence.append([min(i for i in d.values() if i >= 0), max(d.values())])
        if d[char] != -1:   d = dict((k, -1 if v < d[char] else v) for k,v in d.items())
        d[char] = index
        if index == 1:      sequence.append([min(i for i in d.values() if i >= 0), max(d.values())])
    return max([i[1]-i[0]+1 for i in sequence]) if len(s) > 1 else (1 if len(s) == 1 else 0)








a = length('kwwkew')
b = length('inconsistent')
c = length('au')
d = length('ccc')
e = length('q&')
