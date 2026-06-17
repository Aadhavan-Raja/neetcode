class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        start = l
        end = l-1
        n = len(nums)
        while start % n < end % n:
            mid = (l + r) // 2
            if nums[mid % n] > target:
                end = mid
            elif nums[mid % n] < target:
                start = mid + 1
            else:
                return mid
        return -1