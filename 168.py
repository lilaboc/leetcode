# https://leetcode.com/problems/excel-sheet-column-title/

from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber != 0:
            columnNumber, m = divmod(columnNumber - 1, 26)
            result.append(ascii_uppercase[m])
        return ''.join(result[::-1])


# print(Solution().convertToTitle(1))
# print(Solution().convertToTitle(26))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(2147483647))
