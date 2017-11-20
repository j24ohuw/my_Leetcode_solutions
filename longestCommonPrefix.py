class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        for char in range(len(strs[0])):
            for i in strs[1:]:
                try:
                    if strs[0][char] != i[char]:
                        return strs[0][:char]
                except:
                    return strs[0][:char]
        return strs[0]
