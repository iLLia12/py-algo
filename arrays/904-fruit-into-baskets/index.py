class Solution:
    def totalFruit(self, fruits) -> int:
        res = 1
        counter = 1
        bakets = set()
        bakets.add(fruits[0])
        left = 0
        for i in range(1, len(fruits)):
            bakets.add(fruits[i])
            if len(bakets) == 3:
                bakets = set()
                bakets.add(fruits[i])
                bakets.add(fruits[i - 1])
                counter = left + 1
                res = max(res, counter)
            else:
                counter += 1
            res = max(res, counter)
            if fruits[i] != fruits[i - 1]:
                left = 1
            else: left += 1
        return res