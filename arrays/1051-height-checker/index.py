from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        s = [*heights]
        heights.sort()
        for i in range(len(s)):
            if s[i] != heights[i]:
                res += 1
        return res