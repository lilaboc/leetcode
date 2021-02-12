# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        mi = salary[0]
        mx = salary[0]
        t = salary[0]
        for i in salary[1:]:
            if i < mi:
                mi = i
            if i > mx:
                mx = i
            t += i
        return (t - mi - mx) / (len(salary) - 2)


print(Solution().average([6000,5000,4000,3000,2000,1000]))