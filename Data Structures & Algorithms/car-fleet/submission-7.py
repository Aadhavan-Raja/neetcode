class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        res = 0
        prev_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            if time > prev_time:
                res += 1
                prev_time = time
        
        return res
