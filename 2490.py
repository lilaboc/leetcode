# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        parts = sentence.split(' ')
        if len(parts) == 1:
            return parts[0][-1] == parts[-1][0]
        for i in range(len(parts) - 1):
            if parts[i][-1] != parts[i + 1][0]:
                return False
        return parts[-1][-1] == parts[0][0]



print(Solution().isCircularSentence("leetcode exercises sound delightful"))
print(Solution().isCircularSentence("Leetcode is cool"))
