# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        cs = set(c1.keys()).union(set(c2.keys()))
        for i in cs:
            if abs(c1.get(i, 0) - c2.get(i, 0)) > 3:
                return False
        return True


print(Solution().checkAlmostEquivalent("aaaa", "bccb"))
print(Solution().checkAlmostEquivalent("abcdeef", "abaaacc"))
print(Solution().checkAlmostEquivalent("cccddabba", "babababab"))