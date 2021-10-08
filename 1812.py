# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = "abcdefgh".index(coordinates[0]) + 1
        y = int(coordinates[1])
        return x % 2 != y % 2


print(Solution().squareIsWhite("a1"))
print(Solution().squareIsWhite("h3"))

