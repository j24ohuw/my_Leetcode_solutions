class Solution:
    def opposite(self, char):
        if char == '}': return '{'
        if char == ']': return '['
        if char == ')': return '('
        
    def isValid(self, s):
        if len(s) == 0 or len(s) == 1: return False
        L = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                L.append(i)
            try:
                if (i == '}' or i == ')' or i == ']'):
                    if L.pop() != self.opposite(i):
                        return False
            except:
                return False   
        return True if len(L) == 0 else False   
