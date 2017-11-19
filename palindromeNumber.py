import math
class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        if x < 10: return True
        for i in range(0,math.ceil(math.log10(x)/2)):
            if int(x/(10**i)) % 10 != int((x/(10**int(math.log10(x)-i)))%10): return False
        return True
        
