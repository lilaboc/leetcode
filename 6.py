# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        length = len(s)
        for lineNum in range(numRows):
            for o in range(lineNum, len(s), numRows * 2 - 2):
                result += s[o]
                if lineNum != 0 and lineNum != numRows - 1:
                    pos = o + numRows * 2 - 2 * lineNum -2
                    if pos < length and pos > 0:
                        result += s[pos]
        return result




print(Solution().convert("PAYPALISHIRING", 5))