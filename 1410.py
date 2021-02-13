# https://leetcode.com/problems/html-entity-parser/

import re

class Solution:
    def entityParser(self, text: str) -> str:
        d = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<", "&frasl;": "/"}
        parts = re.split("(" + "|".join(d.keys()) + ")", text)
        result = ""
        for i in parts:
            if i in d.keys():
                result += d[i]
            else:
                result += i
        return result

print(Solution().entityParser("&amp; is an HTML entity but &ambassador; is not."))
