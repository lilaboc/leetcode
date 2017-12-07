# https://leetcode.com/problems/battleships-in-a-board/description/
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        previous = []
        count = 0
        for i in xrange(len(board)):
            ship = False
            for o in xrange(len(board[0])):
                if board[i][o] == 'X' and not ship:
                    ship = True
                    if i == 0 or board[i - 1][o] != 'X':
                        count += 1
                elif board[i][o] == '.':
                    ship = False
                

        return count


