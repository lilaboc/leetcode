# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 1:
            return 0
        a, b = Counter(s[0]), Counter(s[1:])
        count = 1 if len(a.keys()) == len(b.keys()) else 0
        for i in s[1:]:
            a[i] += 1
            b[i] -= 1
            if b[i] == 0:
                del b[i]
            if len(a.keys()) == len(b.keys()):
                count += 1
        return count



print(Solution().numSplits("aacaba"))
print(Solution().numSplits("aaaaa"))