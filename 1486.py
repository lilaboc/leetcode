# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        r = arr[0]
        for i in arr[1:]:
            r ^= i
        return r

print(Solution().xorOperation(1, 7))
