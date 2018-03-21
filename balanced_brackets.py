#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

brackets = {'(':')',
                   '[':']',
                   '{':'}'}

def is_matched(expression):
    if len(expression) % 2 != 0: return False
    if len(expression) == 0 :    return True
    
    array = []
    for i in expression:
        if i not in '()[]{}':
            return False
        if i in brackets.keys():
            array.append(i)
        else:
            if len(array) >= 1:
                if brackets[array.pop()] != i:
                    return False
            else:
                return False
    return True if len(array) == 0 else False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
