# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        elif len(strs) == 1:
            return strs[0]
        for i in range(min(map(len, strs))):
            if all(map(lambda x: strs[0][i] == x[i], strs[1:])):
                result += strs[0][i]
            else:
                break
        return result

        


print(Solution().longestCommonPrefix(["flower","flow","flight"]))