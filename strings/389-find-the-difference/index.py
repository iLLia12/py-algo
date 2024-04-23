class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        m = {}
        for i in t:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in s:
            if i in m:
                m[i] -= 1
        for i in m:
            if m[i] != 0:
                return i