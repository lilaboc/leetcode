# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        r = []
        for i in s:
            if i != '*':
                r.append(i)
            else:
                r.pop()
        return ''.join(r)


print(Solution().removeStars("leet**cod*e"))
print(Solution().removeStars("erase*****"))