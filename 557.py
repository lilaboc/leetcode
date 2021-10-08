# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        r = []
        for i in s.split(' '):
            r.append(i[::-1])
        return " ".join(r)

print(Solution().reverseWords("Let's take LeetCode contest"))