 # https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        ss = set()
        count = 0
        for i in s:
            if i not in ss:
                ss.add(i)
            else:
                count += 1
                ss = set(i)
        return count + 1


print(Solution().partitionString("abacaba"))