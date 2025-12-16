# https://leetcode.com/problems/restore-finishing-order/description/
from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s = set(friends)
        return [i for i in order if i in s]

print(Solution().recoverOrder([3,1,2,5,4],  [1,3,4]))
print(Solution().recoverOrder([1,4,5,3,2], [2,5]))

