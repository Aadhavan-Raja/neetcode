class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = -num[i]
            while l < r:
                while num[l] + num[r] < target and l < r:
                    l += 1
                while num[l] + num[r] > target and l < r:
                    r -= 1
                if num[l] + num[r] == target:
                    res.append([i, l, r])