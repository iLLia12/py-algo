class Solution:
    def longestPalindrome(self, s: str):
        m = {}
        count = 0
        for char in s:
            if char not in m or m[char] == 0:
                m[char] = 1
            else:
                m[char] -= 1
                count += 1
        res = count * 2
        if len(s) - res != 0:
            res += 1
        return res