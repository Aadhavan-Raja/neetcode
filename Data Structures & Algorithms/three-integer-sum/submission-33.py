class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                while nums[l] + nums[r] > target and l < r:
                    r -= 1
                while nums[l] + nums[r] < target and l < r:
                    l += 1
                if nums[l] + nums[r] == target and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])  
                l += 1
                r -= 1         
        return res