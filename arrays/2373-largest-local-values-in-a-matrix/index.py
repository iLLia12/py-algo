from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        i = 1
        while len(grid) >= i + 2:
            j = 1
            cur = []
            while len(grid) >= j + 2:
                cur1 = 0
                for i1 in range(3):
                    for i2 in range(3):
                        print(grid[(i - 1) + i1][(j - 1) + i2])
                        cur1 = max(cur1, grid[(i - 1) + i1][(j - 1) + i2])
                cur.append(cur1)
                j += 1
            res.append(cur)
            i += 1
        return res