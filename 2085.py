# https://leetcode.com/problems/count-common-words-with-one-occurrence/
from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = Counter(words1)
        b = Counter(words2)
        count = 0
        for i in a:
            if a[i] == 1 and b[i] == 1:
                count += 1
        return count

