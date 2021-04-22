# https://leetcode.com/problems/word-break/

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.seen = {}
        return any((self.breakable(s[len(i):]) for i in wordDict if s[:len(i)] == i))
    
    def breakable(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if s in self.seen:
            return self.seen[s]
        # print(s)
        result = any((self.breakable(s[len(i):]) for i in self.wordDict if s[:len(i)] == i))
        self.seen[s] = result
        return result

        
    


print(Solution().wordBreak('leetcode', ['leet', 'code']))
#print Solution().wordBreak('leetcode', ['leetc', 'leet', 'code'])
#print Solution().wordBreak('leetcode', ['lee', 'code'])
# print(Solution().wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]))
