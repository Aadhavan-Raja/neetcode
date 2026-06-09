class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefs = [1] * len(nums)
        suffs = [1] * len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            prefs[i] = nums[i] * prefs[i-1]
        for i in range(len(nums) - 1, 0, -1):
            suffs[i] = nums[i] * suffs[i-1]
        for i in range(len(nums)):
            res[i] = prefs[i] * suffs[i]
        return res