# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution:
    def minOperations(self, n: int) -> int:
        a = [2 * i + 1 for i in range(n)]
        avg = sum(a) / len(a)
        return int(sum(abs(avg - i) for i in a) / 2)


print(Solution().minOperations(3))
print(Solution().minOperations(6))