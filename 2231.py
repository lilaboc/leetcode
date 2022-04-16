# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/


class Solution:
    def largestInteger(self, num: int) -> int:
        e = []
        o = []
        for i in str(num):
            if int(i) % 2 == 0:
                e.append(int(i))
            else:
                o.append(int(i))
        e.sort()
        o.sort()
        r = ''
        for i in str(num):
            if int(i) % 2 == 0:
                r += str(e.pop())
            else:
                r += str(o.pop())
        return int(r)

print(Solution().largestInteger(65875))





