#https://leetcode.com/problems/unique-morse-code-words://leetcode.com/problems/unique-morse-code-words/
from typing import List
import string

letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = set()
        for word in words:
            result.add(''.join([letters[string.ascii_lowercase.index(letter)] for letter in word]))
        return len(result)


print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
