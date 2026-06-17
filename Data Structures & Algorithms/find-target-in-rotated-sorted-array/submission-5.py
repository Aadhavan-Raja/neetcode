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
        n = len(nums)
        start = l
        end = l + n -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid % n] > target:
                end = mid - 1
            elif nums[mid % n] < target:
                start = mid + 1
            else:
                return mid % n
        return -1