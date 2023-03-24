# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min, max = -1, -1
        for i in nums:
            if min == -1:
               min = i
            elif i < min:
                min = i
            if i > max:
                max = i
        return gcd(min, max)
    
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b,a % b)

print(Solution().findGCD([2,5,6,9,10]))


