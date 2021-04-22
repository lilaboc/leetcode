# https://leetcode.com/problems/positions-of-large-groups/

from typing import List

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) == 0:
            return []
        prev = S[0]
        start = 0
        result = []
        for i, v in enumerate(S):
            if v != prev:
                if i - start >= 3:
                    result.append([start, i - 1])
                prev = v
                start = i
        if len(S) - start >= 3:
            result.append([start, len(S) - 1])
        return result



print(Solution().largeGroupPositions("abbxxxxzzy"))
print(Solution().largeGroupPositions("abcdddeeeeaabbbcd"))
print(Solution().largeGroupPositions("aaa"))