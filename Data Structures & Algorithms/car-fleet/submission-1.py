class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carLocs = [-1] * (target + 1)
        times = []
        res = 0
        for i in range(len(position)):
            carLocs[position[i]] = speed[i]
        for i in range(len(carLocs)):
            if carlocs[i] != -1:
                time = (target-i) / carLocs[i]
                if stack and time <= stack[0]:
                    stack.append(time)
                else:
                    stack.clear()
                    res += 1
                    stack.append(time)
        return res