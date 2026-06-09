class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        permMap = {}        
        for i in s1:
            s1map[i] = s1map.get(i, 0) + 1
        l = 0
        for r in range(len(s1)):
            permMap[r] = permMap.get(r, 0) + 1
        for r in range(len(s1), len(s2)):
            if permMap == s1map:
                return True
            else:
                permMap[r] = permMap.get(r, 0) + 1
                permMap[l] -= 1
                l += 1
        return False
                
            