# https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        rows = {}
        scores = []
        for row in score:
            rows[row[k]] = row
            scores.append(row[k])
        scores.sort(reverse=True)
        result = []
        for i in scores:
            result.append(rows[i])
        return result

print(Solution().sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2))



