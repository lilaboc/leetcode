# https://leetcode.com/problems/unique-number-of-occurrences/


from typing import List
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(set(c.values())) == len(c.keys()) 

print(Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(Solution().uniqueOccurrences([1,2]))