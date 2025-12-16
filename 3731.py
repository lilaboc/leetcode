# https://leetcode.com/problems/find-missing-elements/description/
from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = 999
        biggest = 0
        s = set()
        for i in nums:
            if i >= biggest:
                biggest = i
            if i <= smallest:
                smallest = i
            s.add(i)
        result = []
        for i in range(smallest + 1, biggest):
            if i not in s:
                result.append(i)
        return result





print(Solution().findMissingElements([1,4,2,5]))
print(Solution().findMissingElements([7,8,6,9]))
print(Solution().findMissingElements([5,1]))
