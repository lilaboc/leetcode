# https://leetcode.com/problems/valid-palindrome/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        l = len(s)
        if l % 2 == 0:
            return s[: int(l/2)] == s[int(l/2):][::-1]
        else:
            return s[: int(l/2)] == s[int(l/2) + 1:][::-1]



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))