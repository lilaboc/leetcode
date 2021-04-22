# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

from typing import List

class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        setList = [set(i) for i in favoriteCompanies]
        result = []
        for i in range(len(setList)):
            found = False
            for o in range(len(setList)):
                if i != o:
                    if setList[i].issubset(setList[o]):
                        found = True
                        break
            if not found:
                result.append(i)
        return result

                
            
        


print(Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))