# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one = False
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1 or one:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    one = True
                else:
                    one = False
            if i == 0 and one:
                digits.insert(0, 1)
        return digits




print(Solution().plusOne([4,3,2,1]))
print(Solution().plusOne([9,9,9,9]))