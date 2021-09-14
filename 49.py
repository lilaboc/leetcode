# https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda: [])
        for i in strs:
            d[''.join(sorted(i))].append(i)
        result = []
        for k, v in d.items():
            result.append([i for i in v])
        return result


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))