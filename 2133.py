# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = [set(range(1, len(matrix) + 1)) for i in range(len(matrix))]
        columns = [set(range(1, len(matrix) + 1)) for i in range(len(matrix))]
        print(rows)
        for rn, row in enumerate(matrix):
            for cn, v in enumerate(row):
                if v in rows[rn]:
                    rows[rn].remove(v)
                else:
                    return False
                if v in columns[cn]:
                    columns[cn].remove(v)
                else:
                    return False
        for i in rows:
            if len(i) != 0:
                return False
        for i in columns:
            if len(i) != 0:
                return False
        return True


# Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]])
Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]])

