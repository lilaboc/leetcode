# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        r = []
        for k,v in c.items():
            if v == 1 and k - 1 not in c and k + 1 not in c:
                r.append(k)
        return r


print(Solution().findLonely([1,3,5,3]))



