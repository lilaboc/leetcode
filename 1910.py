# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s


print(Solution().removeOccurrences("daabcbaabcbc", "abc"))