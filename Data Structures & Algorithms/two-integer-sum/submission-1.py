class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, value in enumerate(nums):
            seen[value] = ind
        for num in nums:
            look = target - num
            if look in seen:
                return [seen[num], seen[look]]