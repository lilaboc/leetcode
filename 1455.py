# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, v in enumerate(sentence.split(" ")):
            if v.startswith(searchWord):
                return i + 1
        return -1
        