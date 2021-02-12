# https://leetcode.com/problems/most-common-word/

from typing import List
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        return Counter([i.group(0).lower() for i in re.finditer('\w+', paragraph) if i.group(0).lower() not in banned]).most_common(1)[0][0]
        


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
        