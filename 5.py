# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        window = len(s)
        while True:
            for i in range(len(s) - window + 1):
                st = s[i : i + window]
                if st[:] == st[::-1]:
                    return st
            window -= 1

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("bb"))