# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(i.split(" ")) for i in sentences])


print(Solution().mostWordsFound(["please wait", "continue to fight", "continue to win"]))