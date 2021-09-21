# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1

print(Solution().areOccurrencesEqual("abacbc"))


