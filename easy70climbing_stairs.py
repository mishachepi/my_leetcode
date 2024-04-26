"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_ways(steps_left, ways_to_climb): # Time Limit Exceeded
            if steps_left <= 0:
                if steps_left == 0:
                    ways_to_climb[0] += 1
                return
            for steps in 1, 2:
                climb_ways(steps_left - steps, ways_to_climb)

        ways = [0,]
        climb_ways(n, ways)
        return ways[0]
