class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                return nums[i]
            nums[abs(nums[i]) - 1] *= -1