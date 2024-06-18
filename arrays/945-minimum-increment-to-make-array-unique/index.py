class Solution:
    def minIncrementForUnique(self, nums) -> int:
        res = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i] += 1
                res += 1
            elif nums[i - 1] > nums[i]:
                a = nums[i - 1] - nums[i] + 1
                print(a)
                res += a
                nums[i] += a
        return res