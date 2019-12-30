# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = len(s)
        while True:
            munique = 0
            for i in range(len(s) - window + 1):
                unique = len(set(s[i: i + window])) 
                if unique > munique:
                    munique = unique
            if munique == window:
                return window
            elif munique == 1:
                return 1
            else:
                window = munique
            
        
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
        