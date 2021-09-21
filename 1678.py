# https://leetcode.com/problems/goal-parser-interpretation/

import re

class Solution:
    def interpret(self, command: str) -> str:
        rep = {"()": "o", "(al)": "al"}
        rep = dict((re.escape(k), v) for k, v in rep.items())
        # Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], command)


print(Solution().interpret("(al)G(al)()()G"))
