# https://leetcode.com/problems/distribute-candies-to-people/
from typing import List
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        turn = 0
        while True:
            round = sum(range(turn* num_people + 1, (turn + 1) * num_people + 1))
            if candies > round:
                candies -= round
                turn += 1
            else:
                break
        for i in range(num_people):
            result[i] = sum(range(turn)) * num_people + (i + 1) * turn
            num = turn * num_people + i + 1
            if candies > num:
                result[i] += num
                candies -= num
            else:
                result[i] += candies
                candies = 0
        
        return result

                
#print(Solution().distributeCandies(60, 4))
