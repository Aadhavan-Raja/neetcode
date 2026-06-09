class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                while nums[l] + nums[r] > target and l < r:
                    r -= 1
                while nums[l] + nums[r] < target and l < r:
                    l += 1
                if nums[l] + nums[r] == target and l < r:
                    res.append([nums[i], nums[l], nums[r]])  
                while l < r and nums[l] == nums[l - 1]:
                        l += 1
                while l < r and nums[r] == nums[r + 1]:
                        r -= 1      
        return res