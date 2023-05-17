# https://leetcode.com/problems/keys-and-rooms/
import queue
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [i for i in rooms[0]]
        seen = set()
        seen.add(0)
        while len(q) != 0:
            now = q.pop()
            seen.add(now)
            for i in rooms[now]:
                if i not in seen:
                    q.append(i)
        return len(seen) == len(rooms)



print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
