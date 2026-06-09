class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        water = [0] * len(height)
        for i in range(1, len(height)):
            lmax[i] = max(height[i-1], lmax[i-1])
        for i in range(len(height) - 2, 0, -1):
            rmax[i] = max(height[i+1], rmax[i+1])
        for i in range(len(height)):
            water[i] = min(lmax[i], rmax[i]) - height[i]
        print(lmax)
        print(rmax)
        print(water)
        sum = 0
        for i in water:
            if i > 0:
                sum += i
        return sum
                





            
