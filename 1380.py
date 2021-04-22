# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        allRowCandidates = set()
        for x in range(len(matrix)):
            rowCandidates = set()
            rowCandidates.add((x, 0))
            smallest = matrix[x][0]
            for y in range(len(matrix[x])):
                v = matrix[x][y]
                if v == smallest:
                    rowCandidates.add((x, y))
                elif v < smallest:
                    rowCandidates.clear()
                    rowCandidates.add((x, y))
                    smallest = v
            # print(rowCandidates)
            allRowCandidates = allRowCandidates|rowCandidates
        # print(allRowCandidates)
        allColCandidates = set()
        for y in range(len(matrix[0])):
            colCandidates = set()
            colCandidates.add((0, y))
            largest = matrix[0][y]
            for x in range(len(matrix)):
                v = matrix[x][y]
                if v == largest:
                    colCandidates.add((x, y))
                if v > largest:
                    colCandidates.clear()
                    colCandidates.add((x, y))
                    largest = v
            allColCandidates = allColCandidates|colCandidates
        return [matrix[x][y] for x, y in allRowCandidates.intersection(allColCandidates)]
        # print(allColCandidates)


# print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
            
