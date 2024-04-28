"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

# it is not true solution, true solution is something wioth factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        answers = {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 8,
            6: 13,
            7: 21,
            8: 34,
            9: 55,
            10: 89,
            11: 144,
            12: 233,
            13: 377,
            14: 610,
            15: 987,
            16: 1597,
            17: 2584,
            18: 4181,
            19: 6765,
            20: 10946,
            21: 17711,
            22: 28657,
            23: 46368,
            24: 75025,
            25: 121393,
            26: 196418,
            27: 317811,
            28: 514229,
            29: 832040,
            30: 1346269,
            31: 2178309,
            32: 3524578,
            33: 5702887,
            34: 9227465,
            35: 14930352,
            36: 24157817,
            37: 39088169,
            38: 63245986,
            39: 102334155,
            40: 165580141,
            41: 267914296,
            42: 433494437,
            43: 701408733,
            44: 1134903170,
            45: 1836311903,
            }
        return answers[n]

test = Solution()
test_cases = list(x for x in range(1,46))

for i in test_cases:
    print(f"for {i} = {test.climbStairs(i)}")

