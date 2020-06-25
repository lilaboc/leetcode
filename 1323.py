# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        try:
            i = n.index('6')
            n = n[:i] + '9' + n[i + 1:]
        except:
            pass
        return int(n)

# print(Solution().maximum69Number(9669))
# print(Solution().maximum69Number(9996))
# print(Solution().maximum69Number(9999))