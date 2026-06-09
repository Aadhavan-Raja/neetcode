class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind, value in enumerate(nums):
            seen[value] = ind
        for i, num in enumerate(nums):
            look = target - num
            if look in seen and seen[look] != i:
                return [i, seen[look]]