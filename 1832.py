# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

from collections import Counter

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(Counter(sentence)) == 26


print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(Solution().checkIfPangram("leetcode"))
