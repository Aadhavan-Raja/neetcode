class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carLocs = [-1] * (target + 1)
        times = []
        res = 0
        for i in range(len(position)):
            carLocs[position[i]] = speed[i]
        carLocs.reverse()
        for i in range(len(carLocs)):
            if carLocs[i] != -1:
                time = (target-i) / carLocs[i]
                if times and time <= times[0]:
                    times.append(time)
                else:
                    times.clear()
                    res += 1
                    times.append(time)
        return res