class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        permMap = {}
        if len(s1) > len(s2):
            return False        
        for i in s1:
            s1map[i] = s1map.get(i, 0) + 1
        l = 0
        for r in range(len(s1)):
            permMap[s2[r]] = permMap.get(s2[r], 0) + 1
        for r in range(len(s1), len(s2)):
            if permMap == s1map:
                return True
            else:
                permMap[s2[r]] = permMap.get(s2[r], 0) + 1
                permMap[s2[l]] -= 1  
                if permMap[s2[l]] == 0:
                    del permMap[s2[l]]
                l += 1
            if permMap == s1map:
                return True
        print(list(s1map.items()))
        print(list(permMap.items()))                
        return False
                
            