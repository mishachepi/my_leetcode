"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:

        def climb_ways(steps_left):
            if steps_left <= 0:
                if steps_left == 0:
                   return 1
                return 0
            ways = 0
            for steps in 1, 2:
                ways += climb_ways(steps_left - steps)
            return ways

        return climb_ways(n)

test = Solution()
test_cases = [0, 1 , 2, 10, 40]

for i in test_cases:
    print(test.climbStairs(i))
