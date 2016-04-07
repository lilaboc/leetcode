# https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])
        if not self.is_valid_shape(board, height, width):
            return False

        rows = [set() for _ in xrange(height)]
        columns = [set() for _ in xrange(width)]
        subboxes = [[set() for _ in xrange(width / 3)] for _ in xrange(height / 3)]
        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if value == '.':
                    continue
                if value in rows[y] or value in columns[x] or value in subboxes[x / 3][y / 3]:
                    return False
                rows[y].add(value)
                columns[x].add(value)
                subboxes[x / 3][y / 3].add(value)
        return True

    def is_valid_shape(self, board, height, width):
        for i in board:
            if len(i) != width:
                return False
        if width % 3 != 0 or height % 3 != 0:
            return False
        return True

#print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
