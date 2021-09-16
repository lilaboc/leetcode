# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self._isIsomorphic(s, t) and self._isIsomorphic(t, s)

    def _isIsomorphic(self, s, t):
        d = {}
        for i, o in zip(t, s):
            if i not in d:
                d[i] = o
            elif d[i] != o:
                return False
        return True




print(Solution().isIsomorphic("badc", "baba"))
print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("foo", "bar"))
print(Solution().isIsomorphic("paper", "title"))

