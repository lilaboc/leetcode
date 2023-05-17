# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        r = []
        for k, v in Counter(s).most_common():
            r.append(v * k)
        return "".join(r)


print(Solution().frequencySort("tree"))
