# https://leetcode.com/problems/maximum-product-of-two-digits/description/
class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(str(n))
        return int(n[-2]) * int(n[-1])

print(Solution().maxProduct(124))

