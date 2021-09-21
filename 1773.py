# https://leetcode.com/problems/count-items-matching-a-rule/
from typing import List
from collections import defaultdict


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        t = defaultdict(lambda: 0)
        c = defaultdict(lambda: 0)
        n = defaultdict(lambda: 0)
        for i, v in enumerate(items):
            t[v[0]] += 1
            c[v[1]] += 1
            n[v[2]] += 1
        return {"type": t, "color": c, "name": n}[ruleKey].get(ruleValue, 0)


print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))
print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))