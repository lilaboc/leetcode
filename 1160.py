# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        c = Counter(chars)
        for w in words:
            i = Counter(w)
            if all([i[o] <= c[o] for o in i.keys()]):
                result += len(w)
        return result


print(Solution().countCharacters(["cat","bt","hat","tree"], "atach"))
print(Solution().countCharacters( ["hello","world","leetcode"], "welldonehoneyr"))

        