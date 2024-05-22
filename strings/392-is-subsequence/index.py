class Solution:
    def isSubsequence(self, s: str, t: str):
        if s == "":
            return True
        j = -1
        for i in t:
            if i == s[j + 1]:
                j += 1
            if j == len(s) - 1:
                return True
        return False