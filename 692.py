# https://leetcode.com/problems/top-k-frequent-words/


from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))][:k]


# print(Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 2))
# print(Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 3))
print(Solution().topKFrequent(["aaa","aa","a"], 1))