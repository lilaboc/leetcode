# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        vowel = 0
        consonant = 0

        for k, v in c.most_common():
            if vowel == 0 and k in 'aeiou':
                vowel = v
            elif consonant == 0 and k not in 'aeiou':
                consonant = v
            if vowel != 0 and consonant != 0:
                break
        return vowel + consonant

print(Solution().maxFreqSum('successes'))




