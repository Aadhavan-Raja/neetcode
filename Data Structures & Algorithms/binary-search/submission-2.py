class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums):
            if len(nums) == 1:
                if nums[0] == target:
                    return nums[0]
                else:
                    return -1
            if len(nums) == 0:
                return -1
            mid = len(nums) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                return binarySearch(nums[mid+1: len(nums)])
            elif nums[mid] >= target:
                return binarySearch(nums[0: mid])