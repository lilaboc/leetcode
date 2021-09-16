# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/


from typing import List 
from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = Counter()
        for i in time:
            c[i % 60] += 1
        count = 0
        for i in c.keys():
            if (i == 30 or i == 0) and c[i] > 1:
                count += sum(range(c[i]))
            elif i < 30:
                count += c[i] * c[60 - i]
        return count

    

# print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
# print(Solution().numPairsDivisibleBy60([60, 60, 60]))
# print(Solution().numPairsDivisibleBy60([418,204,77,278,239,457,284,263,372,279,476,416,360,18]))
print(Solution().numPairsDivisibleBy60([309,148,402,199,180,170,293,72,165,318,178,444,105,265,311,223,242,11,341,232,37,90,214,73,15,431,82,323,291,296,234,32,21,156,235,379,275,273,69,91,275,93,281,212,478,365,126,457,268,85,217,144,325,376,357,457,129,189,140,384,21,342,416,34,252,216,311,228,380,149,123,276,458,225,271,489,125,377,440,459,428,52,372,337,55,1,183,214,42,174,193,196,230,144,213,292,34,8,61,432,23,24,128,416,136,196,290,406,103,394,408,97,222,418,122,94,171,214,418,458,141,356,212,217,428,183,488,471,29,441,190,133,152,448,390,40,180,28,156,43,299,251,250,48,423,437,417,303,81,284,448,459,30,273,141,111,61,366,157,434,155,114,208,423,56,8,95,461,351,448,244,244,121,112,374,267,26,176,203,24,142,98,372,208,438,335,432,456,161,157,353,161,235,395,389,208]))
            
            