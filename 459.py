# https://leetcode.com/problems/repeated-substring-pattern/


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors = [i for i in range(1, int(len(s) / 2) + 1) if len(s) % i == 0]
        for factor in factors:
            if s[:factor] * int(len(s) / factor) == s:
                return True
        return False



print(Solution().repeatedSubstringPattern("abcabcabcabc"))