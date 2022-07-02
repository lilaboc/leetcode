# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = Counter(s)
        target = Counter(target)
        return min([int(s[i]/target[i]) for i in target])


print(Solution().rearrangeCharacters("ilovecodingonleetcode", "code"))
print(Solution().rearrangeCharacters("abbaccaddaeea", "aaaaa"))

