class Solution:
    def lengthOfLongestSubstring(self, s):
        basket = []
        len_seq = 0
        for i in s:
            if i not in basket:
                basket.append(i)
                if len(basket) > len_seq: len_seq = len(basket)
            else:
                basket = basket[basket.index(i)+1:]
                basket.append(i)
        return len_seq
