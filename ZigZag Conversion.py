class Solution:
    def convert(self, s, R):
        if len(s) == 0 or R == 1: return s
        if R == 2: return s[0::2]+s[1::2]
        sheet = {i:[] for i in range(R)}
        current = 0
        while True:
            #vertical
            for i in range(R): #2*R-1)
                sheet[i].append(s[current])
                if current < len(s)-1:
                    current += 1
                else:
                    return ''.join([''.join(sheet[i]) for i in sheet.keys()])
            for i in range(1,R-1)[::-1]:
                sheet[i].append(s[current])
                if current < len(s)-1:
                    current += 1
                else:
                    return ''.join([''.join(sheet[i]) for i in sheet.keys()])
