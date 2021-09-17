# https://leetcode.com/problems/decode-string/
import re
class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = self.onepass(s)
        return s

    def onepass(self, s: str) -> str:
        for i in re.finditer("(?P<count>\d+)\[(?P<repeat>[a-z]+)\]", s, re.I | re.M | re.S):
            s = s.replace(i.group(0), i.group('repeat') * int(i.group('count')))
        return s



# print(Solution().decodeString("3[a]2[bc]"))
# print(Solution().decodeString("abc3[cd]xyz"))
# print(Solution().decodeString("abc3[cd]xyz"))
print(Solution().decodeString("3[a2[c]]"))



