class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        pre = list(strs[0])
        for i in strs[1:]:
            e = 0
            while True:
                if e > min(len(pre),len(i))-1:  
                    pre = pre[:e]
                    break
                if pre[e] == i[e]:              
                    e += 1
                else:              
                    pre = pre[:e]
                    break

        return ''.join(pre) if len(pre) != 0 else ""
