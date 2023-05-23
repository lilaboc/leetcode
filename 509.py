# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def __init__(self):
        self.r = [0, 1]
        for i, o in zip(range(29), range(1, 30)):
            self.r.append(self.r[i] + self.r[o])

    def fib(self, n: int) -> int:
        return self.r[n]

print(Solution().fib(4))