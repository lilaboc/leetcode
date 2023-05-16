# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for q in queries:
            r = 0
            count = 0
            for i in nums:
                if r + i <= q:
                    r += i
                    count += 1
            result.append(count)
        return result

print(Solution().answerQueries([4,5,2,1], [3,10,21]))

